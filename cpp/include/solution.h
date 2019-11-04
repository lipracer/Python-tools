
#include <iostream>
#include <vector>
#include <chrono>
#include <thread>
#include <string>
#include <list>

using namespace std;
using namespace chrono;

/*
huawei question:
example aBBbb123aca
output:
a=3
B=2
b=2
c=1
∏ˆ ˝œ‡µ»∞¥’’œ»≥ˆœ÷œ»¥Ú”°
*/

struct char_info
{
	int count;
	int first_appear_index;
	char value;
	char_info() : count(0), first_appear_index(-1) {}
};
void computer_count(const string& str);

struct DNode
{
    DNode *prevNode;
    DNode *nextNode;
    void *data;
};
typedef DNode* pDNode;

template <typename T>
struct TreeNode
{
    TreeNode *leftNode;
    TreeNode *rightNode;
    T data;
    
    TreeNode() : leftNode(nullptr), rightNode(nullptr)
    {
        
    }
};

template <typename T>
class SearchTree
{
    typedef TreeNode<T> Node;
public:
    void insert(Node node)
    {
        if(!head)
        {
            head = new Node();
            *head = node;
            return;
        }
        Node *_tmpNode = new Node(node);
        inset_node(head, _tmpNode);
    }
    //中序遍历
    void ergodic()
    {
        
    }
private:
    TreeNode<T>* head;
    void inset_node(Node *cur_node, Node *targetNode)
    {
        if (targetNode->data < cur_node->data)
        {
            if(nullptr == cur_node->leftNode)
            {
                cur_node->leftNode = targetNode;
                return;
            }
            inset_node(cur_node->leftNode, targetNode);
        }
        if (targetNode->data > cur_node->data)
        {
            if(nullptr == cur_node->rightNode)
            {
                cur_node->rightNode = targetNode;
                return;
            }
            inset_node(cur_node->rightNode, targetNode);
        }
    }
};
