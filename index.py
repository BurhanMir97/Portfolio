# =========================================
# LOVE WEBSITE - FINAL WORKING VERSION
# =========================================
#
# STEP 1:
# Install Flask
#
# pip install flask
#
# STEP 2:
# Save this file as:
#
# app.py
#
# STEP 3:
# Run:
#
# python app.py
#
# STEP 4:
# Open in browser:
#
# http://127.0.0.1:5000
#
# =========================================

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():

    return """
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width,
               initial-scale=1.0">

<title>For My Love ❤️</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">

<style>

*{
  margin:0;
  padding:0;
  box-sizing:border-box;
  font-family:'Poppins',sans-serif;
}

body{

  overflow:hidden;

  height:100vh;

  display:flex;
  justify-content:center;
  align-items:center;

  background:
  linear-gradient(
  135deg,
  #0f0c29,
  #302b63,
  #24243e
  );

  position:relative;

  color:white;
}

/* STARS */

.star{

  position:absolute;

  width:2px;
  height:2px;

  background:white;

  border-radius:50%;

  opacity:0.7;

  animation:twinkle 3s infinite;
}

@keyframes twinkle{

  0%,100%{
    opacity:0.2;
  }

  50%{
    opacity:1;
    transform:scale(2);
  }
}

/* HEARTS */

.heart{

  position:absolute;

  color:pink;

  animation:floatUp linear infinite;
}

@keyframes floatUp{

  from{
    transform:
    translateY(100vh)
    rotate(0deg);

    opacity:0;
  }

  10%{
    opacity:1;
  }

  to{
    transform:
    translateY(-120vh)
    rotate(360deg);

    opacity:0;
  }
}

/* CARD */

.card{

  width:90%;
  max-width:500px;

  padding:40px;

  border-radius:30px;

  background:
  rgba(255,255,255,0.08);

  backdrop-filter:blur(10px);

  text-align:center;

  box-shadow:
  0 0 40px rgba(255,105,180,0.3);

  position:relative;

  z-index:2;

  animation:floatCard 4s infinite ease-in-out;
}

@keyframes floatCard{

  0%,100%{
    transform:
    translateY(0px);
  }

  50%{
    transform:
    translateY(-10px);
  }
}

h1{

  font-size:3rem;

  margin-bottom:20px;
}

.message{

  line-height:1.9;

  font-size:1rem;

  margin-bottom:30px;
}

.question{

  font-size:2rem;

  margin-bottom:40px;
}

/* BUTTONS */

.buttons{

  position:relative;

  width:100%;

  height:220px;
}

button{

  position:absolute;

  border:none;

  border-radius:16px;

  padding:16px 28px;

  font-size:18px;

  cursor:pointer;

  transition:0.1s linear;

  min-width:130px;
}

/* YES BUTTON */

#yesBtn{

  left:10%;
  top:40%;

  background:
  linear-gradient(
  135deg,
  #ff4f81,
  #ff7eb3
  );

  color:white;

  z-index:2;

  box-shadow:
  0 0 20px rgba(255,105,180,0.5);
}

/* NO BUTTON */

#noBtn{

  right:10%;
  top:40%;

  background:
  rgba(255,255,255,0.15);

  color:white;

  z-index:3;
}

/* FINAL SCREEN */

.ending{

  display:none;

  position:fixed;

  inset:0;

  background:
  linear-gradient(
  135deg,
  #ff5c8d,
  #ff2d68
  );

  justify-content:center;
  align-items:center;
  flex-direction:column;

  z-index:999;

  text-align:center;

  padding:30px;
}

.ending h2{

  font-size:4rem;

  margin-bottom:20px;
}

.ending p{

  font-size:1.3rem;

  line-height:1.8;
}

</style>

</head>

<body>

<div class="card">

  <h1>
    Hey Love ❤️
  </h1>

  <div class="message">

    I know I can be difficult sometimes.<br><br>

    I know there are moments where
    I seem distant or disconnected...<br><br>

    But I swear,
    you are always on my mind.<br><br>

    Somehow,
    my heart always finds its way back to you.

  </div>

  <div class="question">

    Do you love me? 🌸

  </div>

  <div class="buttons">

    <button id="yesBtn">
      Yes ❤️
    </button>

    <button id="noBtn">
      No 😢
    </button>

  </div>

</div>

<div class="ending" id="ending">

  <h2>
    I KNEW IT ❤️
  </h2>

  <p>

    Thank you for loving me.<br><br>

    My heart will always choose you.

  </p>

</div>

<script>

// STARS

for(let i=0;i<70;i++){

  const star =
  document.createElement("div");

  star.classList.add("star");

  star.style.left =
  Math.random()*100 + "vw";

  star.style.top =
  Math.random()*100 + "vh";

  star.style.animationDuration =
  (2 + Math.random()*5) + "s";

  document.body.appendChild(star);
}

// HEARTS

const hearts =
["❤","💕","💖","♡"];

for(let i=0;i<20;i++){

  const heart =
  document.createElement("div");

  heart.classList.add("heart");

  heart.innerHTML =
  hearts[Math.floor(Math.random()*hearts.length)];

  heart.style.left =
  Math.random()*100 + "vw";

  heart.style.fontSize =
  (16 + Math.random()*18) + "px";

  heart.style.animationDuration =
  (8 + Math.random()*10) + "s";

  heart.style.animationDelay =
  Math.random()*5 + "s";

  document.body.appendChild(heart);
}

// BUTTONS

const noBtn =
document.getElementById("noBtn");

const yesBtn =
document.getElementById("yesBtn");

const ending =
document.getElementById("ending");

let scale = 1;

// MOVE NO BUTTON

function moveNoButton(){

  const maxX =
  window.innerWidth -
  noBtn.offsetWidth - 20;

  const maxY =
  window.innerHeight -
  noBtn.offsetHeight - 20;

  const randomX =
  Math.random() * maxX;

  const randomY =
  Math.random() * maxY;

  noBtn.style.position =
  "fixed";

  noBtn.style.left =
  randomX + "px";

  noBtn.style.top =
  randomY + "px";

  // YES BUTTON GETS BIGGER

  scale += 0.35;

  yesBtn.style.transform =
  `scale(${scale})`;

  yesBtn.style.boxShadow =
  `0 0 ${20 + scale*10}px
   rgba(255,105,180,0.8)`;

  // FULLSCREEN MODE

  if(scale > 6){

    yesBtn.style.position =
    "fixed";

    yesBtn.style.left = 0;

    yesBtn.style.top = 0;

    yesBtn.style.width =
    "100vw";

    yesBtn.style.height =
    "100vh";

    yesBtn.style.borderRadius =
    "0";

    yesBtn.style.fontSize =
    "60px";

    yesBtn.style.zIndex =
    "9999";

    yesBtn.innerHTML =
    "PRESS ME ❤️";
  }
}

// DESKTOP

noBtn.addEventListener(
  "mouseover",
  moveNoButton
);

// MOBILE

noBtn.addEventListener(
  "touchstart",
  function(e){

    e.preventDefault();

    moveNoButton();
  }
);

// YES BUTTON

yesBtn.addEventListener(
  "click",
  function(){

    ending.style.display =
    "flex";
  }
);

</script>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
