// your JavaScript file
const container = document.querySelector('#container');

const content = document.createElement('div');
content.classList.add('content');
content.textContent = 'This is the glorious text-content!';

container.appendChild(content);

const p = document.createElement('p');
p.classList.add('para')
container.appendChild(p);
p.style.color='red';
p.innerHTML = "<p>Hey I'm red!</p>";  

const blue = document.createElement('h3');
blue.classList.add('para');
container.appendChild(blue);
blue.style.color = 'blue';
blue.innerHTML = "<h3>Hey I'm blue h3!</h3>";




/*
a <p> with red text that says “Hey I’m red!”
an <h3> with blue text that says “I’m a blue h3!”
a <div> with a black border and pink background color with the following elements inside of it:
another <h1> that says “I’m in a div”
a <p> that says “ME TOO!”
Hint for this one: after creating the <div> with createElement, append the <h1> and <p> to it before adding it to the container.
*/

