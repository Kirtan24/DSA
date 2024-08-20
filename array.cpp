#include <iostream>

using namespace std;

// Display
void displayArray(int arr[], int size) {
    cout << "Array elements: ";
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

// Insert at Beaginning
void insertAtBeginning(int arr[], int &size, int element) {
    for (int i = size; i > 0; i--) {
        arr[i] = arr[i - 1];
    }
    arr[0] = element;
    size++;
}

// Insert at Ending
void insertAtEnding(int arr[], int &size, int element) {
    arr[size] = element;
    size++;
}

// Insert at Specific Location
void insertAtSpecific(int arr[], int &size, int element, int position) {
    if (position > size || position < 0) {
        cout << "Invalid position!" << endl;
        return;
    }
    for (int i = size; i > position; i--) {
        arr[i] = arr[i - 1];
    }
    arr[position] = element;
    size++;
}

// Delete Element
void deleteElement(int arr[], int &size, int position) {
    if (position >= size || position < 0) {
        cout << "Invalid position!" << endl;
        return;
    }
    for (int i = position; i < size - 1; i++) {
        arr[i] = arr[i + 1];
    }
    size--;
}

// Search
int findElement(int arr[], int size, int element) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == element) {
            return i;
        }
    }
    return -1;
}

// Update Element at Specific Position
void updateElement(int arr[], int size, int element, int position) {
    if (position >= size || position < 0) {
        cout << "Invalid position!" << endl;
        return;
    }
    arr[position] = element;
}

// Main Function
int main() {
    int arr[100];
    int size = 0;
    int choice, ichoice, element, position;

    while (true) {
        cout << "\nArray Operations Menu:\n";
        cout << "1. Insert Element\n";
        cout << "2. Delete Element\n";
        cout << "3. Find Element\n";
        cout << "4. Display Array\n";
        cout << "5. Update Element\n";
        cout << "0. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                while(true){
                    cout << "\nInsert Operations:\n";
                    cout << "1. Insert Element at Beginning\n";
                    cout << "2. Insert Element at Ending\n";
                    cout << "3. Insert Element at Specific Location\n";
                    cout << "0. Back\n";
                    cout << "Enter your choice: ";
                    cin >> ichoice;
                    if (ichoice == 0) {
                        break;
                    }
                    cout << "Enter element to insert: ";
                    cin >> element;
                    switch (ichoice) {
                        case 1:
                            insertAtBeginning(arr, size, element);
                            break;
                        case 2:
                            insertAtEnding(arr, size, element);
                            break;
                        case 3:
                            cout << "Enter position to insert (0-based index): ";
                            cin >> position;
                            insertAtSpecific(arr, size, element, position);
                            break;
                        default:
                            cout << "Invalid choice! Please try again." << endl;
                            break;
                    }
                }
                break;
            }
            case 2: {
                cout << "Enter position to delete (0-based index): ";
                cin >> position;
                deleteElement(arr, size, position);
                break;
            }
            case 3: {
                cout << "Enter element to find: ";
                cin >> element;
                position = findElement(arr, size, element);
                if (position != -1) {
                    cout << "Element found at position: " << position << endl;
                } else {
                    cout << "Element not found in the array." << endl;
                }
                break;
            }
            case 4: {
                displayArray(arr, size);
                break;
            }
            case 5: {
                cout << "Enter position to update (0-based index): ";
                cin >> position;
                cout << "Enter new element: ";
                cin >> element;
                updateElement(arr, size, element, position);
                break;
            }
            case 0: {
                cout << "Exiting..." << endl;
                return 0;
            }
            default: {
                cout << "Invalid choice! Please try again." << endl;
            }
        }
    }
}