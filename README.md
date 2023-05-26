# python-as3toplevel
A python implementation of some of the ActionScript3 toplevel functions and classes. They are as close as I could get them with my knowledge and the very limited documentation that adobe provides. The types (Array, Boolean, Number, and String) are actual types so you can use them as such. They include almost everything that they did in ActionScript3.
The length method is just to return the length so it can't be assigned as it can in ActionScript3
The inherited properties in ActionScript3 are too complex for me to implement or aren't documented very well so I won't be implementing most of them.
Since it is hard to have a class and function with the same name, I put the conversion functions inside of their respective class (ex: instead of String(expression) to convert to string, use String.String(expression)).
