document.getElementById("startGame").addEventListener("click", function() {
    fetch("/start-game", { method: "POST" })
        .then(response => response.json())
        .then(data => {
            document.getElementById("maskedWord").innerText = data.maskedWord;
            document.getElementById("remainingGuesses").innerText = data.remainingGuesses;
            document.getElementById("guessedLetters").innerText = data.guessedLetters.join(", ");
        });
});

document.getElementById("submitGuess").addEventListener("click", function() {
    let guess = document.getElementById("guessInput").value;
    document.getElementById("guessInput").value = "";

    fetch("/make-guess", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            letter: guess,
            word: document.getElementById("maskedWord").dataset.word,
            maskedWord: document.getElementById("maskedWord").innerText,
            guessedLetters: document.getElementById("guessedLetters").innerText.split(", "),
            remainingGuesses: parseInt(document.getElementById("remainingGuesses").innerText)
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("maskedWord").innerText = data.maskedWord;
        document.getElementById("remainingGuesses").innerText = data.remainingGuesses;
        document.getElementById("guessedLetters").innerText = data.guessedLetters.join(", ");
        document.getElementById("message").innerText = data.message;
    });
});
