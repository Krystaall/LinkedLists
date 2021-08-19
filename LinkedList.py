class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)  # node(data,next) here data=data and next=self.head
        self.head = node  # new head is the node just inserted

    def print(self):
        if self.head is None:
            print('The list is empty')
            return

        itr = self.head
        llstr = ''  # creating new linkedlist string just to print it
        while itr:
            llstr += str(itr.data) + ' -> '
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def create_new_ll(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index > self.length():
            raise Exception('INVALID INDEX')

        if index == 0:  # if we want remove head element
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.length():
            raise Exception('INVALID INDEX')
        if index == 0:  # if we want insert head element
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

        itr = itr.next
        count += 1

    def insert_after_value(self, data_after, data_to_insert):
        present = None

        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            present = 1
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                present = 1
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

        if present is None:
            print('DATA NOT PRESENT')

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next=itr.next.next
                break
            itr = itr.next







if __name__ == '__main__':  # this is like main block
    ll = LinkedList()
    ll.insert_at_begining(1)
    ll.insert_at_begining(2)
    ll.insert_at_begining(3)
    ll.insert_at_end(4)
    ll.print()

    ll2 = LinkedList()
    ll2.create_new_ll(['mango', 'apple', 'banana'])
    ll2.print()
    print(ll2.length())
    ll2.remove_at(1)
    ll2.print()
    ll2.insert_at(1, 'kiwi')
    ll2.print()

    ll2.insert_after_value('mango', 'peaches')
    ll2.print()
    ll2.insert_after_value('br', 'pear')
    ll2.print()

    ll2.remove_by_value('mango')
    ll2.print()
