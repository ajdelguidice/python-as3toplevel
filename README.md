# python-as3toplevel
Do not use version 0.0.3. I forgot to remove the stuff I used for debugging
<br><br>A python implementation of some of the ActionScript3 toplevel functions and classes. They are as close as I could get them with my knowledge and the very limited documentation that adobe provides.
<br><br>The types (Array, Boolean, Int, Number, and String) are actual types so you can use them as such. They include almost everything that they did in ActionScript3. The length method in each type can only be used to get the length, I didn't implement the length assignment for Arrays.
<br><br>Most of the inherited properties would be too hard to implement so I didn't bother with them.
<br><br>I implemented the type conversion functions inside the types themselves (ex: instead of String(expression) use String.String(expression)).
<br><br>For functions that needed a placeholder value for input(s) that aren't easily definable, like multiple possible types or they relied on other factors to be set, I use an empty dictionary as a placeholder. The values that these empty dictionaries represent aren't actually dictionaries, I just used something that would never be used in these functions so that I could detect it.
<br><br>I have no way as of current to test the accuracy of these functions as I can't find a compiler for actionscript that I could get to work so if anything doesn't work or there is undocumented functionality please let me know on the github page.
<br><br>
# Config Files
<br>&lt;library-directory&gt;/mm.cfg - this file is the same as it was in actionscript with the same options as defined [here](https://web.archive.org/web/20180227100916/helpx.adobe.com/flash-player/kb/configure-debugger-version-flash-player.html) with the exception of "ClearLogsOnStartup" which I added to configure what it says. Its defualt value if 1 to match the behavior in actionscript.
<br><br>
# Currently Implemented
<br>ArgumentError(Error Class)
<br>Array(Function) - Moved to Array.Array()
<br>Array(Data Type)
<br>&emsp;Array(Constructor) - Create from values moved to class init function, create to size moved to toSize(Function).
<br>&emsp;length(Property) - Moved to length(Function).
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
<br>DefinitionError(Error Class)
<br>Error(Error Class)
<br>EvalError(Error Class)
<br>int(Data Type) - Moved to Int
<br>&emsp;toExponential(Function)
<br>&emsp;toFixed(Function)
<br>isFinite(Function)
<br>isNaN(Function)
<br>valueOf(Function)
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
<br>&emsp;valueOf(Function)
<br>RangeError(Error Class)
<br>ReferenceError(Error Class)
<br>SecurityError(Error Class)
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
<br>SyntaxError(Error Class)
<br>trace(Function) - To use trace first use the "EnableDebug" command that I added. I also changed the default file path to be flashlog.txt in the directory of this library. If you want the log file to be anywhere different, use the TraceOutputFileName definition in mm.cfg
<br>TypeError(Error Class)
<br>URIError(Error Class)
<br>VerifyError(Error Class)
<br><br>
# Partially Implemented
<br>Date(Data Type)
<br>escape(Function)
<br>Number(Data Type)
<br>&emsp;toString(Function)
<br>int(Data Type)
<br>&emsp;toString(Function) - Don't know what is supposed to happen when radix is outside of the given range (not documented)
<br>Number(Data Type)
<br>&emsp;toExponential(Function)
<br>String(Data Type)
<br>&emsp;substr(Function) - Don't know what happens when startIndex is outside of string (not documented)
<br>unescape(Function)
<br><br>
# Future Plans
<br>Array(Data Type)
<br>&emsp;sort(Function)
<br>&emsp;sortOn(Function)
<br>Date(Function)
<br>Date(Data Type)
<br>decodeURI(Function)
<br>decodeURIComponent(Function)
<br>encodeURI(Function)
<br>encodeURIComponent(Function)
<br>int(Function)
<br>int(Data Type)
<br>&emsp;toPrecision(Function)
<br>RegExp(Data Type)
<br>Number(Data Type)
<br>&emsp;toExponential(Function)
<br>&emsp;toFixed(Function)
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
<br>uint(Function)
<br>uint(Data Type)
<br>Vector(Function)
<br>Vector(Data Type)
<br><br>
# Functions I added
<br>listtoarray - converts a given list to an Array. Returns the Array.
<br>Array.toSize - Creates an Array to specified size. If nothing is specified, assumes 0 elements
<br>Dunder methods to relavent data types
<br>defaultTraceFilePath - returns the default file path for logs
<br>defaultTraceFilePath_Flash - returns the default file path for logs in actionscript
<br>EnableDebug - enables "debug mode". Debug mode is something from actionscript that was enabled by using the debug version of the interpreter. Since python doesn't have a debug interpreter, this function is used to enable the debug capabilities of things in this library (only the documented ones).
<br>DisableDebug - disables "debug mode"
<br>formatTypeToName - takes a type object and converts it to a string without the name of the package it came from (&lt;class 'as3.Array'&gt; becomes "Array")
