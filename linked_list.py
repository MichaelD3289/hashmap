from typing import Any, Optional, Union


class KvNode:
    def __init__(self, key: str, data: Any, next_: Optional["KvNode"] = None) -> None:
        self.key = key
        self.data = data
        self.next = next_

    def __repr__(self):
        return self.key


class Bucket:
    def __init__(self) -> None:
        self.head: Union[KvNode, None] = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(f"{node.key}")
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def append(self, node: KvNode):
        if self.head is None:
            self.head = node
            return

        for current_node in self:
            pass

        current_node.next = node

    def remove(self, target_node_key: str):
        if self.head is None:
            raise Exception("Bucket is empty")

        if self.head.key == target_node_key:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.key == target_node_key:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception(f"Node with key `{target_node_key}` not found")
