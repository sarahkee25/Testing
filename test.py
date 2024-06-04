import json
from typing import List

# DO NOT MODIFY THIS CLASS!
class Node():
    def  __init__(self,
                  key        = None,
                  keycount   = None,
                  leftchild  = None,
                  rightchild = None):
        self.key        = key
        self.keycount   = keycount
        self.leftchild  = leftchild
        self.rightchild = rightchild

# DO NOT MODIFY THIS FUNCTION!
# For the tree rooted at root, dump the tree to stringified JSON object and return.
# NOTE: in future projects you'll need to write the dump code yourself,
# but here it's given to you.
def dump(root: Node) -> str:
    def _to_dict(node) -> dict:
        return {
            "key": node.key,
            "keycount": node.keycount,
            "leftchild": (_to_dict(node.leftchild) if node.leftchild is not None else None),
            "rightchild": (_to_dict(node.rightchild) if node.rightchild is not None else None)
        }
    if root == None:
        dict_repr = {}
    else:
        dict_repr = _to_dict(root)
    return json.dumps(dict_repr,indent = 2)

#---------------------------------------------------------------------------------------------------

# For the tree rooted at root and the key given:
# If the key is not in the tree, insert it with a keycount of 1.
# If the key is in the tree, increment its keycount.
def insert(root: Node, key: int) -> Node:
    if root == None:
        return Node(key = key, keycount = 1, leftchild = None, rightchild = None)
    elif key == root.key:
        root.keycount += 1
    elif key > root.key: 
        root.rightchild = insert(root.rightchild, key)
    else: # key < root.key
        root.leftchild = insert(root.leftchild, key)

    return root

# For the tree rooted at root and the key given:
# If the key is not in the tree, do nothing.
# If the key is in the tree, decrement its key count. If they keycount goes to 0, remove the key.
# When replacement is necessary use the inorder successor.
def delete(root: Node, key: int) -> Node:
    if root == None: # empty tree
        return root
    elif key == root.key:
        # delete key and replace if necessary using the inorder successor
        if root.keycount == 1:
            # remove key here

            if root.leftchild == None: # element to delete has no left child
               return root.rightchild
            elif root.rightchild == None: # element to delete has no right child
                return root.leftchild
            else: # element to delete has 2 children
                # use inorder successor (find smallest value (min key) in right subtree)
                smallestRight = root.rightchild
                
                # find the smallest value in the right subtree of the root (inorder successor)
                while smallestRight.leftchild != None:

                    # copy smallest value in right subtree to the element to delete
                    # root.key = smallestRight.key
                    # root.keycount = smallestRight.keycount
                    smallestRight = smallestRight.leftchild

                root.key = smallestRight.key
                root.keycount = smallestRight.keycount
                smallestRight.keycount = 1

                # recursively call delete() to remove the inorder successor from the tree, will continue until base case is hit
                root.rightchild = delete(root.rightchild, root.key)

        else: # key count > 1, so just decrement key count by 1
            root.keycount -= 1
    elif key > root.key: 
        root.rightchild = delete(root.rightchild, key)
    else: # key < root.key
        root.leftchild = delete(root.leftchild, key)

    return root

# For the tree rooted at root and the key given:
# Calculate the list of keys on the path from the root towards the search key.
# The key is not guaranteed to be in the tree.
# Return the json.dumps of the list with indent=2.
def search(root: Node, search_key: int) -> str:
    list = []

    while root != None:
        list.append(root.key)
        if search_key == root.key:
            return(json.dumps(list, indent=2))
        elif search_key < root.key:
            root = root.leftchild
        else: # search_key > root.key
            root = root.rightchild

    return(json.dumps(list, indent=2))

# Helper method for preorder
def prehelp(root: Node, list): # root L R
    if root != None:
        list.append(root.key)
        prehelp(root.leftchild, list)
        prehelp(root.rightchild, list)

# For the tree rooted at root, find the preorder traversal.
# Return the json.dumps of the list with indent=2.
def preorder(root: Node) -> str:
    list = []
    prehelp(root, list)

    return(json.dumps(list, indent=2))

# Helper method for inorder
def inhelp(root: Node, list): # L root R
    if root != None:
        inhelp(root.leftchild, list)
        list.append(root.key)
        inhelp(root.rightchild, list)

# For the tree rooted at root, find the inorder traversal.
# Return the json.dumps of the list with indent=2.
def inorder(root: Node) -> str:
    list = []
    inhelp(root, list)

    return(json.dumps(list, indent=2))

# Helper method for postorder
def posthelp(root: Node, list): # L R root
    if root != None:
        posthelp(root.leftchild, list)
        posthelp(root.rightchild, list)
        list.append(root.key)

# For the tree rooted at root, find the postorder traversal.
# Return the json.dumps of the list with indent=2.
def postorder(root: Node) -> str:
    list = []
    posthelp(root, list)
   
    return(json.dumps(list, indent=2))