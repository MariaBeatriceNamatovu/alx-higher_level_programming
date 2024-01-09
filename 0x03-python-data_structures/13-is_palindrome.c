#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of the first node of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev = NULL, *next, *temp;

    if (*head == NULL || (*head)->next == NULL)
        return (1);  // An empty list or a single-node list is a palindrome

    // Move fast and slow pointers to find the middle of the list
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        // Reverse the first half of the list while finding the middle
        temp = slow;
        slow = slow->next;
        temp->next = prev;
        prev = temp;
    }

    // If the number of nodes is odd, skip the middle node
    if (fast != NULL)
        slow = slow->next;

    // Compare the reversed first half with the second half
    while (slow != NULL)
    {
        if (slow->n != prev->n)
            return (0);  // Not a palindrome

        slow = slow->next;
        prev = prev->next;
    }

    return (1);  // Palindrome
}

