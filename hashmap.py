from curses import BUTTON1_CLICKED
import math
from re import L
from typing import Any

from linked_list import Bucket, KvNode


class HashMap:
    def __init__(self) -> None:
        self.size = 0
        self.capacity = 2
        self.load_factor = 0.7
        self.table = [Bucket() for _ in range(self.capacity)]

    def __str__(self) -> str:
        repr_ = "{\n"

        for bucket in self.table:
            for item in bucket:
                repr_ += f'\t"{item.key}": '
                if isinstance(item.data, str):
                    repr_ += f'"{item.data}",\n'
                else:
                    repr_ += f"{item.data},\n"

        repr_ += "}"
        return repr_

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.add(key, value)

    def __delitem__(self, key):
        self.remove(key)

    def _hashkey(self, key: str) -> int:
        key_hash = hash(key)
        return key_hash % self.capacity

    def _capacity(self):
        if self.size >= self.capacity * self.load_factor:
            return self.capacity * 2

        half_capacity = math.floor(self.capacity / 2)
        if self.size < half_capacity * self.load_factor:
            return half_capacity

        return self.capacity

    def _resize(self):
        new_capacity = self._capacity()

        if new_capacity == self.capacity:
            return

        self.capacity = new_capacity

        new_table = [Bucket() for _ in range(self.capacity)]

        for bucket in self.table:
            for item in bucket:
                index = self._hashkey(item.key)
                new_table[index].append(KvNode(item.key, item.data))

        self.table = new_table

    def get(self, key: str) -> Any:
        key_index = self._hashkey(key)

        bucket = self.table[key_index]
        for item in bucket:
            if item.key == key:
                return item.data

        raise KeyError(f"'{key}' not found")

    def add(self, key: str, value: Any):
        key_index = self._hashkey(key)

        bucket = self.table[key_index]

        if bucket.head is None:
            bucket.append(KvNode(key=key, data=value))
            self.size += 1
            self._resize()
            return

        for item in bucket:
            if item.key == key:
                item.data = value
                return

        bucket.append(KvNode(key=key, data=value))
        self.size += 1
        self._resize()

    def remove(self, key: str):
        key_index = self._hashkey(key)
        try:
            bucket = self.table[key_index]
            bucket.remove(key)
        except Exception:
            raise KeyError(f"'{key}' not found")

        self.size -= 1
        self._resize()
