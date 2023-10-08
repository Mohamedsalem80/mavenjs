# mavenjs v1.0.2
an open-sourced JavaScript library that eases creation and manipulation of web applications.

---
[Download mavenjs v1.0.2](https://github.com/Mohamedsalem80/mavenjs/archive/refs/tags/v1.0.2.zip)

## OR
### Customize using builder
- Run `builder.py`
- It will show `MavenJS: `
- write `build-mavenjs` to start the building `MavenJS: build-mavenjs`
- From here we have to paths
    - Write `*` to build the full version `MavenJS: build-mavenjs *` hit enter and it will generate a js file containing the code
    - Write `core` to build library core `MavenJS: build-mavenjs core` then
    - Write the functions you want `MavenJS: build-mavenjs core add on css slideToggle` hit enter and it will generate a js file containing the code

---

## Examples:

### Select all divs 
```js
var divs = mvn("div");
```

### Select all elements with container class
```js
var containers = mvn(".container");
```
### Select all divs with container class
```js
var divs = mvn("div.container");
```

### Apply CSS properties to elements
```js
mvn(".red").css("color", "red");
```
## Further more:

| Functions  | Version   | Description |
| ---------- | --------- | ----------- |
| add | v1.0.0 | Adds an old maven object to the new object |
| toArray | v1.0.0 | Returns an array from the maven object |
| ready | v1.0.0 | Takes a function and run it when the page is done loading |
| on | v1.0.0 | Attaches a function to elements given event  |
| off | v1.0.0 | Dettaches a function from element at certain event  |
| css | v1.0.0 | Manipulates elements css properties |
| scroll | v1.0.0 | Attaches a function to scroll on given elements |
| scrollTo | v1.0.0 | Scrolls to given coordinates |
| html | v1.0.0 | If string is passed changes element html content to it else return elements html content as a list |
| text | v1.0.0 | If string is passed changes element text content to it else return elements text content as a list |
| trigger | v1.0.0 | Triggers a given event |
| each | v1.0.0 | Loops over the selected elements with given function |
| map | v1.0.0 | Maps over the selected elements with given function |
| slice | v1.0.0 | Slices the maven object |
| find | v1.0.0 | Fined elements using css selctor by SELECTAR |
| filter | v1.0.0 | Filters selected elements |
| is | v1.0.0 | Filters selected elements by comarison |
| not | v1.0.0 | Filters selected elements by diversion |
| contains | v1.0.0 | Filters selected elements by content |
| has | v1.0.0 | Filters selected elements by atteributes |
| children | v1.0.0 | Returns elements childern as a list |
| parents | v1.0.0 | Returns elements parents as a list |
| siblings | v1.0.0 | Returns elements siblings as a list |
| nextAll | v1.0.0 | Returns elements next siblings as a list |
| prevAll | v1.0.0 | Returns elements previos siblings as a list |
| show | v1.0.0 | Sets element display to none |
| hide | v1.0.0 | Sets elements display to block |
| empty | v1.0.0 | Empties elements content |
| remove | v1.0.0 | Removes elements |
| append | v1.0.0 | Add html content at the end element |
| prepend | v1.0.0 | Add html content at the beggining element |
| after | v1.0.0 | Add html content after an element |
| before | v1.0.0 | Add html content before an element |
| addClass | v1.0.0 | Add class to elements class list |
| removeClass | v1.0.0 | Removes class to elements class list |
| classToggle | v1.0.0 | Toggles class at elements class list |
| hasClass | v1.0.0 | Checks if element has certain class |
| fadeToggle | v1.0.1 | Animates fade to element |
| slideToggle | v1.0.1 | Animates slide to element |
| val | v1.0.0 | Returns input element value |
| len | v1.0.0 | Returns input element value length |
| submit | v1.0.0 | Submit selected forms |
| serialize | v1.0.0 | Modifies URI given form values |
| removeProp | v1.0.0 | Removes a property from elements |
| prop | v1.0.0 | If a property is given its set to elements else returns property value |
| removeAttr | v1.0.0 | Removes Attribute from elements |
| attr | v1.0.0 | If Attribute is given, it's set to elements else gets attribute from elements |
| data | v1.0.1 | Set or get data from elements |
| addSelf | v1.0.0 | Adds maven object to it self |
| ajax | v1.0.0 | Sets up an ajax request |
| Xss | v1.0.0 | Clears input from cross site scripting attacks through string |
| Import | v1.0.2 | Imports a javascript file into the web page throught a script tag |
| copy | v1.0.2 | Copies a given text to users clipboard |

---

[↑Top](https://github.com/Mohamedsalem80/mavenjs/tree/main#mavenjs-v100)
