class Solution:
    def deleteDuplicates(self, head):
        curr = head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next   # duplicate skip karo
            else:
                curr = curr.next           # aage badho
        
        return head
