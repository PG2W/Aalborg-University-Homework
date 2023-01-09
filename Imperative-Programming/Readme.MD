
## Imperative Programming

### C History
C was developed by Dennis Tichie in 1972 at AT&T Bell Labs in the USA. Historically it's connected to the UNIX operating system. Many other programming languages are inspired by C.


### Top-Down Design with Functions
#### What is Top-Down Design?
In software development, top-down design is a method of designing and building a program by breaking it down into smaller, more manageable pieces. This approach allows you to build a program incrementally, starting with the big picture and then working your way down to the details.

Top-down design involves breaking the program into smaller functions, each of which performs a specific task. This allows you to reuse code and make your program more modular and easier to maintain.

#### Prototypes
In C, a prototype is a declaration of a function that specifies the function's name, return type, and parameter list. Prototypes are used to inform the compiler about the functions that are used in a program, so that the compiler can check that the function calls are valid and generate the correct code.

Prototypes are typically placed in a header file or at the top of a source file before the main function.

Handin3.c:
```C
//Prototype at the top of the program
double trap(double, double, int, binary_f, function_flag);
...
double trap(double a, double b, int n, binary_f f, function_flag flag)
{
    //h = (b-a)/n
    double h = (b-a)/n, area;

    //Function pointer to the sum function
    double (*sum_ptr)(double, double, int, binary_f, function_flag) = &sum;

    //Invoking the function pointer and assigning its result to a variable
    double sum = (*sum_ptr)(a, h, n, f, flag);

    //T=(h/2)*(f(a) + f(b) + 2 * (sum [i=1 ... n] f(x_i) )
    area = (h/2) * (f(a, flag) + f(b, flag) + 2 * sum);

    return area;
}
```
#### Library Functions
"Predefined Functions and Code Reuse:
A primary goal of software engineering is to write error-free code. Code reuse, reusing program fragments that have already been written and tested whenever possible,
is one way to accomplish this goal. Stated more simply, “Why reinvent the wheel?”
C promotes reuse by providing many predefined functions that can be used to
perform mathematical computations. C’s standard math library defines a function
named sqrt that performs the square root computation. The function call in the
assignment statement" - *Problem Solving and Program Design in C*


#### Examples:
- math.h 
- stdio.h
- stdlib.h 
- stdbool.h
etc..

### Selection Structures: if and switch Statements
- Single if statement:
```C
if (condition)
    //code...
```

- if-else statement
```C
if (condition)
    //code...
else
    //code...

if (condition)
    //code...
else if (condition)
    //code...
else
    //code...

```

- Switch statement
```C
switch (int){
    case 0:
    //code...
    break;
    case 1:
    //code...
    break;
    default:
    //code...
}
```

- Exit(value)
```C
exit(0) //program terminates with success
exit(-1) //indicates that the program terminates in failure
```
Note: It's better to use EXIT_FAILURE and EXIT_SUCCESS as arguments to stay universal for all platforms

- Conditional expressions
```C
logicalExpression ? expression1 : expression2
// ? = if condition is true (then)
// : = if condition is false (else)
```

### Iterative controlstructures: Loops
- While Loop
```C
while (condition)
{
    //code...
}
```

- Do While Loop
```C
do {
    //code...
}
while (condition)
```

- For Loop
```C
for (type index = startvalue ; condition ; update index)
{
    //code...
}

// Example
for (int i = 0; i < 10; i++)
{
    printf("Number is: %d", i);
}

// Using the comma operator
for (int i = 0, j = 10; i <= j; i++, j--)
{
    //code...
}
```

- Break/Continue/Return
    - Break is used to break out of a Loop and discontinue it
    - Continue is used to end the commands in the on-going iteration of the loop and continue to the next iteration of the loop.
    - Return is used to stop and return a value from the function

### Parameters
- Functions with Output Parameters
*Problem solving and Program design in C - 343*

Examples from P1 and other assignments:
```C
// Returning values to output parameters defined as arrays
/**
 * This function sets some products on sale in each store.
 *
 * @param store_info An array of structures containing information about the store prices
 */
void set_on_sale(t_store_db store_info[])
{
    // Iterate over the stores
    for (int i = 0; i < MAX_STORES; i++)
    {
        // Iterate over the products in each store
        for (int k = 0; k < MAX_PRODUCTS; k++)
        {
            // Set the product on sale using the random_sale_decider function
            store_info[i].product_onSale[k] = random_sale_decider();
        }
    }
}

// Returning values to output parameters defined as pointers
static void scan_data(char *user_input, char *operator_output, double *operand_output, double accumulator_input) {
    char temp_operator;
    double temp_operand = 0.0;
    bool valid_operation = true;

    split_string_by_space(user_input, &temp_operator, &temp_operand);

    switch(temp_operator){
        case '/':
            if (temp_operand == 0)
                valid_operation = false;
            break;
        case '#':
            if (accumulator_input < 0)
                valid_operation = false;
            break;
        case '!':
            if (accumulator_input == 0)
                valid_operation = false;
            break;
        default:
            break;
    }

    if (((confirm_binary_operator(temp_operator) && temp_operand != 0)
         || confirm_unary_operator(temp_operator)) && valid_operation) {
        *operator_output = temp_operator;
        *operand_output = temp_operand;
        return;
    }
}
```
- Call by reference vs Call by value
Call by reference allows manipulating the addresses to the variables being called (by reference)
where as calling by value, you'd pass in values not neccessarily having any affect on their values at their addresses.

### Arrays and Pointers
- Declaration of pointers:
```C
Syntax:  type * variable_name;
Example: int * p;
```
"The value of the pointer variable p is a memory address. A data item whose address is stored in this variable must be of the specified type." - *Problem Solving and Problem Design in C*

- Pointers to Files
miniproject3.c:
```C
char filename[] = "kampe-2020-2021.txt"; //Defining file name
FILE *file = fopen(filename, "r");       //Pointer to the file

//Checking if the pointer is NULL (file wasn't found)
if (file == NULL) {
    //Outputting error message and returning from the function
    printf("Failed to open input file\n");
    return 1;
}
```

- Function pointers
```C
int x = 10;
int *p = &x;
```
In the example above we see an integer variable with an assigned value of 10. The way the machine interpretes this is by allocating memory to the variable x and writing the value 10 into that memory address. On the next line we see a variable pointing to the address of the variable x. So now the machine interpretes this as allocating memory address to the variable p and assigning it the contents of the variable x. This is in essence what a pointer is. An object that points to a memory address.

A function pointer on the other hand is a bit more complicated.
```C
double (*fn)(double, double);
```
The example above is a declaration of a function pointer that requires a function with two double parameters and a double output. So if we have a function with two double inputs and a single double output then we could assign this functionpointer to that function and use it as a pointer pointing to it. An example of this could be the following;
```C
#include <stdio.h>

double plus (double a, double b){
	return a+b;
}

int main(void){
	double (*fn)(double, double);
	fn = &plus;

	return 0;
}
```

- Arrays in C
An array is a collection of elements of the same type stored in contiguous memory locations.

Arrays can have one or multiple dimensions.

In order to declare an array in C, you need to specify the type of the elements and the number of elements the array will hold. For example:
```C
int arr[10]; // Declares an array "arr" of 10 integers

double arr[5][5]; // Declares a two-dimensional array "arr" of 5x5 doubles
```

In order to access an element of an array, you can use the indexing notation, which is the name of the array followed by the index of the element in square brackets. For example:
```C
arr[0] = 5; // Assigns the value 5 to the first element of the array "arr"

arr[3] = 2.5; // Assigns the value 2.5 to the fourth element of the array "arr"
```
The index of an array always starts at 0 in C.

- Pointers and arrays
In C, arrays and pointers are closely related. In fact, when an array is passed to a function or assigned to another array, it is actually the address of the first element of the array that is being passed or assigned.

When you declare a pointer to a certain type, you can use it to point to an array of that type. For example:
```C
int *ptr; // Declares a pointer "ptr" to an integer
ptr = arr; // Assigns the address of the first element of the array "arr" to the pointer "ptr"
```

When you access an element of an array through a pointer, you can use the dereference operator (*) followed by the index of the element in square brackets. For example:
```C
*ptr = 5; // Assigns the value 5 to the element pointed to by the pointer "ptr"
*(ptr + 3) = 2.5; // Assigns the value 2.5 to the fourth element of the array pointed to by "ptr"
```

- Pointer arithmetic
In C, you can perform arithmetic operations on pointers, just like you can with any other type of variable.

For example, you can increment a pointer to point to the next element of an array. If the pointer is pointing to an element of type T, the increment will be T bytes (T is the size of the type in bytes). For example:
```C
ptr++; // Increments the pointer "ptr" to point to the next element of the array
```

You can also use the subtraction operator to find the distance between two pointers pointing to elements of the same array. For example:
```C
int distance = ptr2 - ptr1; // Calculates the distance (in elements) between the pointers "ptr1" and "ptr2"
```

- Sorting arrays:
There are several ways to sort an array in C. One of the most popular is the quicksort algorithm, which has an average case time complexity of O(n*log(n)).

Here is an example of how you can use the quicksort function from the standard library:

miniproject3.c:
```C
int compare_teams(const void *team1, const void *team2) {
    const Team *t1 = (Team *)team1;
    const Team *t2 = (Team *)team2;
    if (t1->points != t2->points) {
        return t2->points - t1->points;
    }
    int diff1 = t1->goals - t1->goals_against;
    int diff2 = t2->goals - t2->goals_against;
    if (diff1 != diff2) {
        return diff2 - diff1;
    }
    return strcmp(t1->name, t2->name);
}

qsort(teams, num_teams, sizeof(Team), compare_teams);
```

Static and dynamic allocation of memory:

In C, you can allocate memory for variables either statically or dynamically.

Static allocation is done at compile time, and the memory is reserved for the entire lifetime of the program. To allocate memory statically, you can simply declare a variable with a specific type and value. For example:
```C
int x = 5; // Allocates 4 bytes of memory for the integer variable "x" and initializes it with the value 5
```

Dynamic allocation is done at runtime, and the memory is allocated from the heap (a pool of free memory managed by the program). To allocate memory dynamically, you can use the malloc function from the standard library. This function takes a single argument, which is the size of the memory block in bytes, and returns a pointer to the first byte of the allocated block. For example:
```C
int *ptr = malloc(sizeof(int)); // Allocates 4 bytes of memory for an integer and returns a pointer to it
```

When you are finished using dynamically allocated memory, you should deallocate it using the free function from the standard library. This function takes a single argument, which is a pointer to the memory block that you want to deallocate. For example:
```C
free(ptr); // Deallocates the memory block pointed to by "ptr"
```

### Unit Testing
Unit testing refers to testing the smallest testable piece of the software, a
single function. To perform a unit test, we write a short driver function to call
the function tested. The driver function begins by giving values to all input
and input/output parameters. Next comes the call to the function being tested.
After calling the function, the driver should display the function results. - *Problem solving and Program Design in*

In my case doing the courses we were using an integrated development environment named CLion, primarily working with C. In order to unit test with CLion we had to work with cmake, which is a horrendous scripting language, unfortunately one we had to learn. Here is an example of implementing a test with Cmake and executing this test;

```C
#include "time_calc.h"

#define SECONDS_PER_HOUR   (60 * 60)
#define SECONDS_PER_MINUTE (60)

void hours_minutes_seconds(int input, int* hours, int* minutes, int* seconds){
    *hours    = input / SECONDS_PER_HOUR;
    input     = input % SECONDS_PER_HOUR;

    *minutes  = input / SECONDS_PER_MINUTE;
    input     = input % SECONDS_PER_MINUTE;

    *seconds  = input;
}
```

time_calc.h:
```C
void hours_minutes_seconds(int input, int* hours, int* minutes, int* seconds);
```

test_time_calc.c:
```C
#include <assert.h>
#include "../src/time_calc.h"

int main(void){
    /*
     *  Input: 4000 sekunder. Forventet output: 1 timer, 6 minutter og 40 sekunder
        Input: 75 sekunder.   Forventet output: 0 timer, 1 minutter og 15 sekunder
        Input: 3700 sekunder. Forventet output: 1 timer, 1 minutter og 40 sekunder
        Input: 55 sekunder.   Forventet output: 0 timer, 0 minutter og 55 sekunder
        Input: 3661 sekunder. Forventet output: 1 timer, 1 minutter og 1 sekunder
     * */

    int hours, minutes, seconds;

    hours_minutes_seconds(4000, &hours, &minutes, &seconds);
    assert(hours == 1); assert(minutes == 6); assert(seconds = 40);

    hours_minutes_seconds(75, &hours, &minutes, &seconds);
    assert(hours == 0); assert(minutes == 1); assert(seconds = 15);

    hours_minutes_seconds(3700, &hours, &minutes, &seconds);
    assert(hours == 1); assert(minutes == 1); assert(seconds = 40);

    hours_minutes_seconds(55, &hours, &minutes, &seconds);
    assert(hours == 0); assert(minutes == 0); assert(seconds = 55);

    hours_minutes_seconds(3661, &hours, &minutes, &seconds);
    assert(hours == 1); assert(minutes == 1); assert(seconds = 1);

    return 0;
}
```

CMake script to add the test
```
# adding test-cases for point distance

# a (series of) tests is by itself a small program
add_executable(test_time_calc test_time_calc.c)

# we need to link with the library we are testing
target_link_libraries(test_time_calc time_calc)

# this is where we actually add the test
add_test(NAME test_time_calc
        COMMAND test_time_calc)
```

Output:
```
Test timeout computed to be: 10000000
```

### Datatypes
- Enumeration types
Enumeration types are custom types that can be used to create types. Consider the following example;
Problem solving and Program Design in C:
```C
typedef enum{
    entertainment, rent, utilities, food, clothing,
    automobile, insurance, miscellaneous
}expense_t;
``` 
As we can observe from the example above, the enumeration type expense_t now has the values entertainment, rent etc. This is now a type just like int, double or the other existing types. It can be used to create variables of that type of which only the values inside the enumeration type definition can be used. Just like values in an integer can consist of only whole numbers or values in a char can consist of only single characters. 

In the definition of these enumeration types, the elements in the list represent a number starting from 0. So entertainment represents 0, rent represents 1 and so on. To visualise this idea, consider the example below;
```C
#include <stdio.h>

typedef enum
{entertainment, rent, utilities, food, clothing,
automobile, insurance, miscellaneous}
expense_t;

int main(void){
	expense_t expense_variable;

	switch(expense_variable){
		case 0:
			printf("0 represents entertainment");
		break;	

		case 1:
			printf("1 represents rent");
		break;
		
		//etc...
	}
}
```
- Typedefinitions
Typedefinitions provide names to already existing type names. Consider the following example;
```C
typedef int integer;
```

Usage:
```C
integer a, b;
```
So in essence it provides a way to change the name of the type. It can also be used with structs, so instead of declaring each struct variable with the name "struct" infront of the variable name, we can remove the struct by defining a typename. Makes the code a tiny bit cleaner.

### Datastructures
- Records/Structures
A record (also known as a structure or struct) is a composite data type in C that groups together values of different types.
To define a struct in C, you use the struct keyword followed by the name of the struct and the definition of its fields inside curly braces. Each field has a name and a type. For example:
```C
struct Example {
    int x;
    int y;
};

To create a variable of a struct type, you can use the name of the struct followed by a variable name. For example:
```C 
struct Example ex; 
```

- Different variants of structs (unions, structs with bitfilter)
There are several variants of structs in C, each with its own specific purpose and characteristics:
Unions: A union is a special type of struct that allows you to store multiple variables of different types in the same memory location. This is useful when you need to save memory or when you want to manipulate the same memory location in different ways. To define a union, you use the union keyword instead of the struct keyword. For example:
```C
union Example {
    int i;
    float f;
    char c;
};
```

Bitfields: A bitfield is a special type of struct field that allows you to specify the size of the field in bits. This is useful when you want to store a set of flags or a bitmask in a struct. To define a bitfield, you use the : operator followed by the number of bits you want to allocate for the field. For example:
```C
struct Flags {
    unsigned int flag1: 1;
    unsigned int flag2: 1;
    unsigned int flag3: 1;
    unsigned int : 5; // Padding field, not used
};
```

- Arrays of structs and structs with arrays
You can use arrays of structs to store a collection of struct values in contiguous memory locations. To create an array of structs, you can use the same syntax as for any other array, but replacing the type with the name of the struct. For example:
```C
struct Example example[10]; // Declares an array "example" of 10 structs of type "Example"
```

You can also use arrays as fields of a struct. This is useful when you want to store a fixed-size collection of values inside a struct. To define a struct with an array field, you can use the syntax for declaring an array inside the struct definition. For example:
```C
struct Example {
    int size;
    struct AnotherExample example[10];
};
```

- Structs with pointers
Lecture10.pdf moodle:
```C
enum color {red, yellow, green, blue, white, black};
    struct point {
    double x, y;
};

struct curve {
    enum color color;
    int length;
    struct point *points;
};
```

- Relation between structs and classes in OOP
Structs and classes are both ways to define a composite data type with multiple fields of different types. However, structs in C are not considered object-oriented programming (OOP). They just allow you to group values together.