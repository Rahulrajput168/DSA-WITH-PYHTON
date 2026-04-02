class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = [] 
        if root == None: return ans
        st = []
        st.append(root)
        while len(st):
            top = st[-1]
            st.pop()
            ans.append(top.val)
            if top.right != None : st.append(top.right)
            if top.left != None : st.append(top.left)
        return ans    

        
