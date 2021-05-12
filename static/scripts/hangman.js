//create an array of words
var word;               // this will hold the hidden word
var answerArray = [];   //this will hold the word as it is being built (guessed from user)
var remainingLetters;   //this keeps track of how many more letters to guess in the hidden word
var errorCount; //this keeps track of the number of wrong letters and is used in building the hangman
var lettersUsed; //this keeps track of the letters that have been guessed so that no letter can be guessed twice

function newGame(words, levels, hints){
//    var words = [
//        "javascript",
//        "classroom",
//        "amazing",
//        "amarillo"
//    ];






    answerArray = [];   //this will hold the underlines - each underline is replaced by a correctly guessed letter
    let randomVal = Math.floor(Math.random() * words.length);
    word=words[randomVal];  //randomly get a hidden word from the words array
    hint=hints[randomVal];
    remainingLetters = word.length;  //How many letters are in the randomly selected hidden word
    errorCount = 0; //keep track of the number of incorrect guesses
    lettersUsed = " ";//clear out the lettersUsed string to start over for new game. 
    document.getElementById('lettersused').innerHTML = lettersUsed;//get letter from user
    for (var i = 0; i < word.length; i++) {  //build the answerArray -- start out with underscore
        answerArray[i] = "__";
    }
    document.getElementById('hint').innerHTML = `hint: ${hint}`
    document.getElementById('guessword').innerHTML = answerArray.join(" ");//format the answerArray with spaces between
    document.getElementById('Messages').innerHTML = " "; //clear out any messages from previous games
    document.getElementById('hangpics').src = "./static/media/0.jpg"; //start out with an empty gallow
}

function guessIt()
{
    if (word==null || remainingLetters == 0 || errorCount > 5) //make sure that New Game was clicked before a letter guessed
        document.getElementById('Messages').innerHTML = "Click New to start a new game";
    else 
        searchWord(); // if new game clicked -- see if letter is in word
    //Clear out the Input Field
    document.getElementById('letter').value = ""; 
    document.getElementById('letter').focus();
}

function searchWord()
{  
    letter = document.getElementById('letter').value.toUpperCase();//keep all lowercase
    document.getElementById('Messages').innerHTML = " "; //clear out messages
    if (letter.length != 1) //if user entered more than 1 letter
        document.getElementById('Messages').innerHTML = "Enter only ONE letter";
    else { if (lettersUsed.indexOf(letter) != -1) //If letter already been guessed
          document.getElementById('Messages').innerHTML = "You already used that letter";
          else {
            found = findIt(letter); //look to see if letter is in hidden word
            lettersUsed = lettersUsed + letter + ' ';//build letter used string
            document.getElementById('lettersused').innerHTML = lettersUsed; //display it
            if (remainingLetters == 0) //if all letters found
                document.getElementById('Messages').innerHTML = "YOU WON!!";
            else if (found == 'n') //if this letter not found (in error)
                updateMissed();
            }
        }
    
}

//code to look to see if the letter that was entered is in the hidden word
//if so, replace the corresponding underscore in the answerArray with the letter
//be sure to update remainingLetters.  Re-display the answerArray formatted with spaces in-between
    function findIt(letter) {
        var found = 'n';
        for(var x = 0; x < word.length; x++)
    {
            if (word[x].toUpperCase() == letter) {
                answerArray[x] = letter;
                found = 'y';
                remainingLetters--;
            }
    }
    document.getElementById('guessword').innerHTML = answerArray.join(" "); 
    return(found);
}

function updateMissed() //updates error count and displays the corresponding hangman image
{
    errorCount++;
    if (errorCount <= 6)
    {
        var img_name = "./static/media/" + errorCount + ".jpg";
        document.getElementById('hangpics').src = img_name;
    } 
    if (errorCount == 6) //if the entire man is hanged, you lose
        document.getElementById('Messages').innerHTML = "YOU LOSE!!";
    
}