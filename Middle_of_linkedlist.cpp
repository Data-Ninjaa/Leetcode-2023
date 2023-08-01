#include <iostream>
using namespace std;

    ListNode* middleNode(ListNode* head) {
        ListNode* current_node = head;
        ListNode* middle_node = current_node;
        ListNode* temp_node = current_node;
        # a variable to keep track of length of list
        int i = 0;
        while(current_node ->next != NULL)
        {
            current_node = current_node->next;
            i++;
        }
        // identifying middle position 
        //if list has even number of elements
        if ( i % 2 == 0)
        {
            i = i/2;
        }
        // if  list has  odd number of elements
        else
        {
            i = (i/2) +1;
        }
        
	//middle position
        int j = 0;
        while(j!=i)
        {
            middle_node = middle_node->next;
            j++;
        }
        return middle_node;
    }
};
