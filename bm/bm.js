$(document).ready(function () {
    //Fades Teemos away and fades in the shroom
    $("#teemos").fadeOut(1000);
    $("#leShroom").hide().html('<p><img id = "theShroom" src="shroom.png" alt="Shroom">Eat me!</p>').fadeIn(4000);

});

var audio = $("leMusic")[0];
//Was trying to rickroll whoever clicks the shroom. Very last minte unfinished code
$("leShroom").mouseenter(function() {
  audio.play();
});



function playSurprise(){
    //Play music
    var playMusic = '<audio controls> <source src="giveyouup.mp3" type="audio/ogg> </audio>';
    document.getElementById('leMusic').innerHTML = playMusic;
}

//Substitute data, waiting for back-end
var CONST_SERVERS = {
    1:"NA",
    2:"BR",
    3:"EUNE",
    4:"EUW",
    5:"LAN",
    6:"LAS",
    7:"OCE",
    8:"RU",
    9:"TR",
    10:"KR"
}

//Tedious for all 126 champions. Will do later
var CONST_CHAMPIONS = {
    34:"Anivia",
    35:"Shaco",
    1:"Annie"
}

var CONST_TIER = {
    1:"Challenger",
    2:"Masters",
    3:"Diamond",
    4:"Platinum",
    5:"Gold",
    6:"Silver",
    7:"Bronze",
    8:"Unranked"
}

var dataHTML;

function findData(){
    /*When submit is clicked, gets all the data you would want
    Server->Tier Level->Champion->Stats
    Stats are not yet included
    */
    dataHTML="";
    var server = getServer();
    var champion = getChampion();
    var tier = getTier();
    if (server == 0) {
        for(var a in CONST_SERVERS){
            findServer(a);   
            if (tier == 0) {
                for(var b in CONST_TIER){
                    findTier(b);
                    if (champion == 0) {
                        for(var c in CONST_CHAMPIONS){
                            findChampion(c);
                        }
                    }
                    else{
                        findChampion(champion);
                    }
                }
            }
            else{
                findTier(tier);
                if (champion ==0) {
                    for(var c in CONST_CHAMPIONS){
                            findChampion(c);
                    }
                }
            }
        }
    }
    else{
        findServer(server);
        if (tier == 0) {
            for(var b in CONST_TIER){
                findTier(b);
                if (champion == 0) {
                    for(var c in CONST_CHAMPIONS){
                        findChampion(c);
                    }
                }
                else{
                    findChampion(champion);
                }
            }
        }
        else{
            findTier(tier);
            if (champion ==0) {
                for(var c in CONST_CHAMPIONS){
                    findChampion(c);
                }
            }
        }
    }
    document.getElementById('dataDiv').innerHTML = dataHTML;
}

function getServer(){
    //Gets server value
    var a = document.getElementById('server');    
    var server = a.options[a.selectedIndex].value;
    return server;
}
function getChampion(){
    //Gets champion ID
    var a = document.getElementById('champion');
    var champion = a.options[a.selectedIndex].value;
    return champion;
}
function getTier(){
    //Gets tier value
    var a = document.getElementById('tier');    
    var tier = a.options[a.selectedIndex].value;
    return tier;
}
function findServer(server){
    //Add server name into the html
    dataHTML = dataHTML.concat('<h2 id = "serverName">' + CONST_SERVERS[server] + '</h2>');    

}
function findTier(tier){
    //Add Tier Image + name into the html
    dataHTML = dataHTML.concat('<h3 id="TierName" >' +'<img id="tierImages" src="\RankImages\\' + CONST_TIER[tier] + '.png" alt="' + CONST_TIER[tier] + 'Rank">' + CONST_TIER[tier] + '</h3>');
    dataHTML = dataHTML.concat('<br>');
    
}
function findChampion(champion){
    //Add Champion Image and data (later) into the html
    dataHTML = dataHTML.concat('<img id="champPortraits" src="\ChampionIcon\\' + CONST_CHAMPIONS[champion] + 'Square.png" alt="' + CONST_CHAMPIONS[champion] + 'Portrait">');
    dataHTML = dataHTML.concat('<br>');
}








