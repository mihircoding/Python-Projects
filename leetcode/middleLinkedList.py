class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        a = []
        while head:
            a.append(head)
            head = head.next
        return a[len(a)//2]