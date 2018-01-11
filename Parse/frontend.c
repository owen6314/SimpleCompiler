#include <stdio.h>
#include <string.h>

int main(int x, char y, int z)
{
	char TIPS_T[] = "EXPR: %s RESULT: %d\n";
	char expr[] = "1+1*3+5-6#";

	char post[1000];
	char ss[1000];
	char ch;
	int sum;
	int i;
	int t;
	int z;
	int error = 0;
	int top = 0;
	t = 1;
	i = 0;
	ch = expr[i];
	i = i + 1;
	while (ch != '#') 
	{
		if (ch == '+' || ch == '-') 
		{
			while (top != 0 && ss[top] != '(')
			{
				post[t] = ss[top];
				top = top - 1;
				t = t + 1;
			}
			top = top + 1;
			ss[top] = ch;

		} 
		else if (ch == '*' || ch == '/') 
		{
			while (ss[top] == '*'|| ss[top] == '/') 
			{
				post[t] = ss[top];
				top = top - 1;
				t = t + 1;
			}
			top = top + 1;
			ss[top] = ch;
		} 
		else if (ch == '(') 
		{
			top = top + 1;
			ss[top] = ch;
		} 
		else if (ch == ')') 
		{
			while (ss[top] != '(') 
			{
				post[t] = ss[top];
				top = top - 1;
				t = t + 1;
			}
			top =top - 1;
		} 
		else if (ch == ' ')
		{
			z = 1;
		} 
		else 
		{
			while (isdigit(ch) || ch == '.') 
			{
				post[t] = ch;
				t = t + 1;
				ch = expr[i];
				i = i + 1;
			}
			i = i - 1;
			post[t] = ' ';
			t = t + 1;
		}
		ch = expr[i];
		i = i + 1;
	}
	while (top!= 0) 
	{
		post[t] = ss[top];
		t = t + 1;
		top = top - 1;
	}
	post[t] = ' ';
	int newstack[100];
	char newstr[100];
	t=1;
	top=0;
	ch = post[t];
	t=t+1;
	char temp;
	while (ch!= ' ' && error == 0) {
		if (ch == '+') 
		{
			int tempTop;
			tempTop = top - 1;
			newstack[tempTop] = newstack[tempTop] + newstack[top];
			top = top - 1;
		} 
		else if (ch == '-') 
		{
			int tempTop;
			tempTop = top - 1;
			newstack[tempTop] = newstack[tempTop] - newstack[top];
			top = top - 1;
		} 
		else if (ch == '*')
		{
			int tempTop;
			tempTop = top - 1;
			newstack[tempTop] = newstack[tempTop] * newstack[top];
			top = top - 1;
		}
		else if(ch == '/') 
		{
			if (newstack[top] != 0)
			{
				int tempTop;
				tempTop = top - 1;
				newstack[tempTop] = newstack[tempTop] / newstack[top];
			}
			else
			{
				error = 1;
			}
			top = top - 1;
		} 
		else 
		{
			i = 0;
			while (isdigit(ch) || ch == '.') 
			{
				newstr[i] = ch;
				i = i + 1;
				ch = post[t];
				t = t + 1;
			}
			temp = 0;
			newstr[i] = temp;
			top = top + 1;
			newstack[top] = atoi(newstr);
		}
		ch = post[t];
		t = t + 1;
	}
	
	int result;
	result = newstack[top];
	if(error == 0)
	{
		printf(TIPS_T, expr, result);
	}
	else
	{
		printf("error\n");
	}
	return 0;
}
