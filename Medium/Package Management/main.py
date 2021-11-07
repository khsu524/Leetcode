
from __future__ import annotations
from typing import Dict, List


class Software:
    def __init__(self, name) -> Software:
        self.name: str = name
        self.dependencies: List[Software] = []

class PackageManagement:
    def __init__(self) -> PackageManagement:
        self.installed_software: List[Software] = [] # keep tracks of installed software
        self.all_software: Dict[str, Software] = {} # maps name to software       
    
    def get_software(self, software_name: str)  -> Software:
        software = self.all_software.get(software_name)
        if not software:
            software = Software(software_name)
            self.all_software[software_name] = software
        return software 

    def build_deps(self, software_name:str, list_of_deps) -> None:
        software = self.get_software(software_name)
        for dependency in list_of_deps:
            curr_dependency_software = self.get_software(dependency)
            dependencies_of_dependency = curr_dependency_software.dependencies
          
            if software in dependencies_of_dependency:
                print(f"{dependency} depends on {software_name}, ignoring command")
            else:
                software.dependencies.append(curr_dependency_software)
    
    def is_already_installed(self, software_to_check: Software) -> bool:
        return software_to_check in self.installed_software
    
    def install(self, software_to_install: Software) -> None:
        print(f"Installing {software_to_install.name}")
        self.installed_software.append(software_to_install)
    
    def can_remove_software(self, software_to_remove: Software):
        for installed in self.installed_software:
            if software_to_remove in installed.dependencies:
                return False
        return True

    def run(self, inputs: List[str]):
        for inp in inputs:
            print(inp)
            args = inp.split(" ")

            command = args[0]

            if command == "DEPEND":
                software_name = args[1]
                # build out dependency
                self.build_deps(software_name, args[2:])
            elif command == "INSTALL":
                software_name = args[1]
                software_to_install = self.get_software(software_name)

                # check if it is already installed
                if self.is_already_installed(software_to_install):
                    print(f"{software_name} is already installed")
                else:
                    # install dependency first
                    for dependency in software_to_install.dependencies:
                        if not self.is_already_installed(dependency):
                            self.install(dependency)
                    # then install software
                    self.install(software_to_install)
                
            elif command == "REMOVE":
                software_name = args[1]
                software_to_remove = self.get_software(software_name)

                if not self.is_already_installed(software_to_remove):
                    print(f"{software_name} is not installed")
                elif self.can_remove_software(software_to_remove):
                    print(f"Removing {software_name}")
                    # remove software
                    self.installed_software.remove(software_to_remove)

                    # remove dependency
                    removed_software_dependency = software_to_remove.dependencies
                    for deps in removed_software_dependency:
                        if self.can_remove_software(deps):
                            print(f"Removing {deps.name}")
                            self.installed_software.remove(deps)
                else:
                    print(f"{software_name} is still needed")
            elif command == "LIST":
                for installed in self.installed_software:
                    print(installed.name)
            elif command == "END":
                break


if __name__ == "__main__":
    inputs = [
        "DEPEND TELNET TCPIP NETCARD",
        "DEPEND TCPIP NETCARD",
        "DEPEND NETCARD TCPIP",
        "DEPEND DNS TCPIP NETCARD",
        "DEPEND BROWSER TCPIP HTML",
        "INSTALL NETCARD",
        "INSTALL TELNET",
        "INSTALL foo",
        "REMOVE NETCARD",
        "INSTALL BROWSER",
        "INSTALL DNS",
        "LIST",
        "REMOVE TELNET",
        "REMOVE NETCARD",
        "REMOVE DNS",
        "REMOVE NETCARD",
        "INSTALL NETCARD",
        "REMOVE TCPIP",
        "REMOVE BROWSER",
        "REMOVE TCPIP",
        "LIST",
        "END"
        ]
    package = PackageManagement()
    package.run(inputs)