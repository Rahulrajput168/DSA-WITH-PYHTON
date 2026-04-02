lass Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        ans = []
        if root == None : return []
        cur = root
        while cur !=None or len(st) !=0:
            if cur:
                st.append(cur)
                cur = cur.left
            else:
                cur = st[-1]
                st.pop()
                ans.append(cur.val)
                cur = cur.right
        return ans            
             