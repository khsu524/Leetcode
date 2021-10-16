class DoubledNode:
    def __init__(self, key:int, value: int):
        self.key = key
        self.value = value
        self.head  = None
        self.tail  = None

    
class LRUCache:
    def __init__(self, capacity: int):
        self.dummy_head = DoubledNode(None,None)
        self.dummy_tail = DoubledNode(None,None)
        self.capacity = capacity
        self.map = {}
        
        self.dummy_head.tail = self.dummy_tail
        self.dummy_tail.head = self.dummy_head
        
    
    def add_node(self, new_node):
        d_head = self.dummy_head
        
        new_node.tail = d_head.tail
        d_head.tail.head = new_node
        
        d_head.tail = new_node
        new_node.head = d_head
        
    def remove_node(self, node_to_remove):
        # Due to removal, we need to connect node_to_update's head aand tail
        h = node_to_remove.head
        t = node_to_remove.tail
        h.tail = t
        t.head = h

    def get(self, key: int) -> int:
        if key in self.map:
            node_to_inspect =  self.map[key]
            
            # it is not in the front
            if not self.dummy_head.tail == node_to_inspect:
                self.remove_node(node_to_inspect)
                # move the node to the front
                self.add_node(node_to_inspect)
            
            return node_to_inspect.value
            
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node_to_update = self.map[key]
            node_to_update.value = value 
            
            if not self.dummy_head.tail == node_to_update:
                self.remove_node(node_to_update)
                # move the node to the front
                self.add_node(node_to_update)
                
        else:    
            # If this is a new "key", create a node, then store it
            new_node = DoubledNode(key, value)
            self.map[key] = new_node
            self.add_node(new_node)
            
            if len(self.map) > self.capacity:
                # gotta remove the last one
                node_to_remove = self.dummy_tail.head
                self.remove_node(node_to_remove)
                # remove from dict
                self.map.pop(node_to_remove.key)


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)