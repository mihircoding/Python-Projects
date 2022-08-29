class Solution:
    def middleNode(head):
        a = []
        while head:
            a.append(head)
            head = head.next
        return a[len(a)//2]
#saved to git with less changes 