const insults = [
    "You're as useless as the 'ueue' in 'queue'.",
    "If laughter is the best medicine, your face must be curing the world.",
    "You're like a cloud. When you disappear, it's a beautiful day.",
    "I'd agree with you, but then we'd both be wrong.",
    "You're not stupid; you just have bad luck when it comes to thinking.",
    "You're the reason God created the middle finger.",
    "If I wanted to kill myself, I would climb your ego and jump to your IQ.",
    "You're like a software update. Whenever I see you, I think, 'Not now.'",
    "I’d call you a tool, but that implies you’re actually useful.",
    "You're proof that even evolution makes mistakes.",
    "You're not a failure; you're just on the extended plan for success!",
"You have potential—just buried under a mountain of poor decisions!",
"You're a work in progress, but at least you're working on something!",
"If at first you don’t succeed, you’re probably just you!",
"You’re like a diamond in the rough—just a bit rougher than most!"
];

const generateButton = document.getElementById('generate');
const insultDisplay = document.getElementById('insult');

generateButton.addEventListener('click', () => {
    const randomIndex = Math.floor(Math.random() * insults.length);
    insultDisplay.textContent = insults[randomIndex];
});
