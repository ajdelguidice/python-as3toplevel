# python-as3toplevel
A python implementation of some of the ActionScript3 toplevel functions and classes. They are as close as I could get them with my knowledge and the very limited documentation that adobe provides.
<br><br>The types (Array, Boolean, Number, and String) are actual types so you can use them as such. They include almost everything that they did in ActionScript3. The length method in each type can only be used to get the length, I didn't implement the length assignment for Arrays.
<br><br>Most of the inherited properties would be too hard to implement so I didn't bother with them.
<br><br>I implemented the type conversion functions inside the types themselves (ex: instead of String(expression) use String.String(expression)).
<br><br>For functions that needed a placeholder value for input(s) that aren't easily definable, could be multiple types, or relied on other factors to be set I use an empty dictionary as a placeholder. The values that these empty dictionaries represent aren't actually dictionaries, I just used something that would never be used in these functions so that I could detect it.
<br><br>I have no way as of current to test the accuracy of these functions as I can't find a compiler for actionscript that I could get to work so if anything doesn't work or there is undocumented functionality please let me know on the github page.
<br><br>
# Currently Implemented
<br>isFinite
<br>isNaN
<br>Array(Function) - Moved to Array.Array()
<br>Array(Data Type)
<br>&emsp;Array(Constructor) - Create from values moved to class init function, create to size moved to toSize(Function).
<br>&emsp;length(Property) - Moved to length(Function). Length assignment functionality not implemented yet
<br>&emsp;concat(Function)
<br>&emsp;every(Function)
<br>&emsp;filter(Function)
<br>&emsp;forEach(Function)
<br>&emsp;indexOf(Function)
<br>&emsp;insertAt(Function)
<br>&emsp;join(Function)
<br>&emsp;lastIndexOf(Function)
<br>&emsp;map(Function)
<br>&emsp;pop(Function)
<br>&emsp;push(Function)
<br>&emsp;removeAt(Function)
<br>&emsp;reverse(Function)
<br>&emsp;shift(Function)
<br>&emsp;slice(Function)
<br>&emsp;some(Function)
<br>&emsp;splice(Function)
<br>&emsp;toLocaleString(Function)
<br>&emsp;toString(Function)
<br>&emsp;unshift(Function)
<br>Boolean(Function) - Moved to Boolean.Boolean()
<br>Boolean(Data Type) - Data representation changed from "true" and "false" to "True" and "False"
<br>&emsp;Boolean(Constructor) - Moved to class init function
<br>&emsp;toString(Function)
<br>&emsp;valueOf(Function)
<br><br>Math(Class) - All functions in this class had corresponding functions in python
<br>&emsp;E(Constant)
<br>&emsp;LN10(Constant)
<br>&emsp;LN2(Constant)
<br>&emsp;LOG10E(Constant)
<br>&emsp;LOG2E(Constant)
<br>&emsp;PI(Constant)
<br>&emsp;SQRT1_2(Constant)
<br>&emsp;SQRT2(Constant)
<br>&emsp;abs(Function)
<br>&emsp;acos(Function)
<br>&emsp;asin(Function)
<br>&emsp;atan(Function)
<br>&emsp;atan2(Function)
<br>&emsp;ceil(Function)
<br>&emsp;cos(Function)
<br>&emsp;exp(Function)
<br>&emsp;floor(Function)
<br>&emsp;log(Function)
<br>&emsp;max(Function)
<br>&emsp;min(Function)
<br>&emsp;pow(Function)
<br>&emsp;random(Function)
<br>&emsp;round(Function)
<br>&emsp;sin(Function)
<br>&emsp;sqrt(Function)
<br>&emsp;tan(Function)
<br>Number(Function) - Moved to Number.Number()
<br>Number(Data Type)
<br>&emsp;Number(Constructor) - Moved to class init function
<br>&emsp;toFixed(Function)
<br>&emsp;valueOf(Function)
<br>String(Function) - Moved to String.String()
<br>String(Data Type)
<br>&emsp;String(Constructor) - Moved to class init function
<br>&emsp;length(Property) - Moved to length(Function)
<br>&emsp;charAt(Function)
<br>&emsp;charCodeAt(Function)
<br>&emsp;concat(Function)
<br>&emsp;indexOf(Function)
<br>&emsp;lastIndexOf(Function)
<br>&emsp;substring(Function)
<br>&emsp;toLocaleLowerCase(Function)
<br>&emsp;toLocaleUpperCase(Function)
<br>&emsp;toLowerCase(Function)
<br>&emsp;toUpperCase(Function)
<br>&emsp;valueOf(Function)
<br><br>
# Partially Implemented
<br>Number(Data Type)
<br>&emsp;toString(Function)
<br>trace(Function)
<br><br>
# Future Plans
<br>ArgumentError(Error Class)
<br>Array(Data Type)
<br>&emsp;sort(Function)
<br>&emsp;sortOn(Function)
<br>decodeURI(Function)
<br>decodeURIComponent(Function)
<br>encodeURI(Function)
<br>encodeURIComponent(Function)
<br>escape(Function)
<br>Error(Error Class)
<br>EvalError(Error Class)
<br>int(Function)
<br>int(Data Type)
<br>RangeError(Error Class)
<br>ReferenceError(Error Class)
<br>RegExp(Data Type)
<br>Number(Data Type)
<br>&emsp;toExponential(Function)
<br>&emsp;toPrecision(Function)
<br>&emsp;toString(Function)
<br>parseFloat(Function)
<br>parseInt(Function)
<br>String(Data Type)
<br>&emsp;localeCompare(Function)
<br>&emsp;match(Function)
<br>&emsp;replace(Function)
<br>&emsp;search(Function)
<br>&emsp;slice(Function)
<br>&emsp;split(Function)
<br>&emsp;substr(Function)
<br>SyntaxError(Error Class)
<br>TypeError(Error Class)
<br>uint(Function)
<br>uint(Data Type)
<br>unescape(Function)
<br>URIError(Error Class)
<br>Vector(Function)
<br>Vector(Data Type)
<br>VerifyError(Error Class)
<br><br>
# Functions I added
<br>listtoarray - converts a given list to an Array.
<br>Array.toSize - Creates an Array to specified size. If nothing is specified, assumes 0 elements

