var instructions_1a_text = function(){
	var instructions = ["<div align=center>Please read all following instructions very carefully.<br><br>It takes some time, but otherwise you will not know what to do.</div>",
	"<div align=center>In this game, you will be taking a spaceship<br> from earth to look for space treasure on two different planets.<br><br><img style='margin:0px auto;display:block;height:200px' src='../static/img/example_planets.png'/></div>", 
	"<div align=center>Each planet has one alien on it and each alien has its own space treasure mine.<br><br><img style='margin:0px auto;display:block;height:100px' src='../static/img/example_aliens.png'/><br>Once you arrive to each planet, you will ask the alien for space treasure from its mine.</div>",
	"<div align=justify>When you ask the alien, you will find out whether you got treasure, which looks like this:<br><br><img style='margin:0px auto;display:block' src='../static/img/treasure_1.png'/><br>Sometimes, the alien will not bring up any treasure and you'll see an empty circle.</div>",
	"<div align=justify>If an alien has a good mine, it means it can easily dig up a lot of space treasure for you:<br><br><img style='margin:0px auto;display:block' src='../static/img/treasure_5.png'/><br>Another alien might have a bad mine that gives little treasure:<br><br><img style='margin:0px auto;display:block' src='../static/img/treasure_1.png'/><br>The quality of each alien's mine will lie somewhere between these two extremes and will change during the game. Aliens with a good mine might get to a part of the mine that has less treasure, and those with less treasure might find more space treasure later on.<br><br>Changes in an alien's mine will happen slowly. So, you have to focus to get as much treasure as possible by finding the alien with the best mine at each point in time.</div>",
    "<div align=justify>Each time you encounter an alien on a planet, you should press the SPACE key to ask it to mine. You will then see whether you got treasure or antimatter and how much you earned. Try practicing a few times.</div>"];
	return instructions
};

var instructions_1b_text = function(){
	var instructions = ["<div align=center>You may have noticed that this alien's mine started out good, and then became less good over time. The mines of other aliens will all follow a unique pattern.<br><br>To see this, you are going to ask another alien for treasure a few times.</div>"];
	return instructions
};

var instructions_1c_text = function(){
	var instructions = ["<div align=justify>Now that you know about the treasures, you can learn to play the whole game.<br><br>On each trial, you will travel from earth to one of two planets, a green planet and a yellow planet:<br><br><img style='margin:0px auto;display:block;height:200px' src='../static/img/example_planets.png'/></div>",
	"<div align=justify>On each trial, you will choose which spaceship to take. For each choice, you will select from one of two pairs of spaceships:<br><br><img style='margin:0px auto;display:block;height:100px' src='../static/img/example_rockets.png'/><br>You can choose the left spaceship by pressing the 'F' key and the right spaceship by pressing the 'J' key. <br><br>Each spaceship will fly to one of the two planets. For each choice pair, one will fly to the yellow planet, and the other will fly to the green planet.</div>",
	"<div align=justify>Let's practice flying to the planets! First, try to pick the spaceships that will get you to the green planet:<br><br><img style='margin:0px auto;display:block;height:200px' src='../static/img/green_planet.png'/></div>"];
	return instructions
};
var instructions_1d_text = function(){
	var instructions = "<div align=center>Very good!<br><br>Now, try to pick the spaceships that will get you to the yellow planet:<br><br><br><img style='margin:0px auto;display:block;height:200px' src='../static/img/yellow_planet.png'/></div>";
	return instructions
};

var instructions_1e_text = function(){
	var instructions = ["<div align=center>You now know how to fly to the planets and how the space treasure works, so you are ready to practice the full game.<br><br>Each time, you will pick a spaceship to fly to a planet and then ask the alien to mine for you.<br><br>Your goal will be to get as much treasure as possible. You will see your current total score after you visit each planet.</div>",
	"<div align=justify>Hint #1:<br>Remember which aliens have treasure. How good a mine is changes slowly, so an alien that has a lot of treasure to share now will probably be able to share a lot in the near future.<br><br>Hint #2:<br>Remember, each alien has its own mine. Just because one alien has a bad mine, does not mean another has a good mine. Also, there are no funny patterns in how much treasure an alien shares, like every other time you ask, or depending on which spaceship you took. The aliens are not tricking you.<br><br>Hint #3:<br>The spaceship you choose is important because often the alien on one planet is better than the ones on another planet. You can find more treasure by finding the spaceship that takes you to the right planet.</div>",
//	"<div align=justify>We are only going to give you 2 seconds to make each choice. At the beginning that won't seem like very much time and you may find the task difficult. Over time, as you learn to play, you will find that 2 seconds is enough time to make good decisions.<br><br>Our advice is to think carefully about your strategy, but also to trust your instincts. By concentrating throughout the experiment you can increase the number of points you win by a lot. There is an element of chance, but a lot of room for skill as well.<br><br>First you will do 25 practice trials. These don't count, and they have no time limit in order to help you learn. Then, you will do 125 real trials for money and with restricted time. At the end we have a few final questions. All together, this takes most people about 25 minutes.</div>"];
	"<div align=justify>Our advice is to think carefully about your strategy, but also to trust your instincts. By concentrating throughout the experiment you can increase the number of points you win by a lot. There is an element of chance, but a lot of room for skill as well.<br><br>First you will do 25 practice trials. These don't count, and they have no time limit in order to help you learn. Then, you will do 125 real trials for money and with restricted time. At the end we have a few final questions. All together, this takes most people about 25 minutes.</div>"];

	return instructions
};

var instructions_2_text = function(){
	var instructions_2 = ["<div align=justify>Ok, you've finished the practice trials. In the real game, you will find new planets, new aliens and new mines, but the rules and the spaceships will be the same.<br><br>Let's review everything we've learned and then begin playing.<br><br>Remember, you want to find as much space treasure as you can by flying to planets and asking an alien to mine for you. How much treasure comes out of each alien's mine changes slowly over time, so you need to concentrate and be flexible to keep track of which spaceships and aliens are good right now.</div>",
	"<div align=justify>How much bonus money you make is based on how much space treasure you find. You will get a bonus payment of 1 cent for every 2 points you earn. On average people win about £0.75, and some have won more than £2.00.<br><br>The game lasts for 125 trials and you will have two seconds for each choice, and that takes most people about 20 minutes. Good luck!</div>"];
	return instructions_2
}

function createMemberInNormalDistribution(mean,std_dev){
	return mean + (gaussRandom()*std_dev);
}
/*
* Returns random number in normal distribution centering on 0.
* ~95% of numbers returned should fall between -2 and 2
*/
function gaussRandom() {
	var u = 2*Math.random()-1;
	var v = 2*Math.random()-1;
	var r = u*u + v*v;
	/*if outside interval [0,1] start over*/
	if(r == 0 || r > 1) return gaussRandom();

	var c = Math.sqrt(-2*Math.log(r)/r);
	return u*c;

	/* todo: optimize this algorithm by caching (v*c) 
	* and returning next time gaussRandom() is called.
	* left out for simplicity */
}

function shuffle(o){
	for(var j, x, i = o.length; i; j = Math.floor(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
	return o;
}

var images = ['../static/img/earth_planet.png',
'../static/img/earth_stim_1.png',
'../static/img/earth_stim_2.png',
'../static/img/earth_stim_3.png',
'../static/img/earth_stim_4.png',
'../static/img/earth_stim_1_deact.png',
'../static/img/earth_stim_2_deact.png',
'../static/img/earth_stim_3_deact.png',
'../static/img/earth_stim_4_deact.png',
'../static/img/red_planet.png',
'../static/img/red_stim.png',
'../static/img/red_stim_sad.png',
'../static/img/red_stim_deact.png',
'../static/img/purple_planet.png',
'../static/img/purple_stim.png',
'../static/img/purple_stim_sad.png',
'../static/img/purple_stim_deact.png',
'../static/img/green_planet.png',
'../static/img/green_stim.png',
'../static/img/green_stim_sad.png',
'../static/img/green_stim_deact.png',
'../static/img/yellow_planet.png',
'../static/img/yellow_stim.png',
'../static/img/yellow_stim_sad.png',
'../static/img/yellow_stim_deact.png',
'../static/img/treasure_1.png',
'../static/img/treasure_2.png',
'../static/img/treasure_3.png',
'../static/img/treasure_4.png',
'../static/img/treasure_5.png',
'../static/img/treasure_6.png',
'../static/img/treasure_7.png',
'../static/img/treasure_8.png',
'../static/img/treasure_9.png',
'../static/img/noreward.png',
'../static/img/example_rockets.png',
'../static/img/example_aliens.png',
'../static/img/example_planets.png',
];

function save_data(data,prolific_id,participant_id,handle){ 
	
for (i = 0; i < data.length; i++) {
	delete data[i].internal_chunk_id;
	delete data[i].trial_index_global;
	delete data[i].trial_type;
	}
		
	$.ajax({
		type:'post',
		cache: false,
		url: 'http://localhost:5000/taskdone?prolific_id=' + prolific_id + '&participant_id=' + participant_id + '&handle=' + handle, 

		data: {
			prolific_id: prolific_id,
			participant_id: participant_id,
			handle: handle,
			json: JSON.stringify(data),
		},
		dataType: 'json', 
		//success: function(){
		//}// write the result to javascript console
		success: function(output) { console.log(output); } // write the result to javascript console
	});

}


function save_subinfo(data,score,prolific_id,participant_id,handle){
	
for (i = 0; i < data.length; i++) {
	delete data[i].internal_chunk_id;
	delete data[i].trial_index_global;
	delete data[i].trial_type;
	}
	
	var scoreinnovelar = (score/100/2).toFixed(2) 

	$.ajax({
		type: "POST",
	    async: false,
		cache: false,
		// url: 'http://localhost:5000/done?prolific_id=' + prolific_id + '&participant_id=' + participant_id + '&handle=' + handle, 
		url: 'https://api-brainexp.osc-fr1.scalingo.io/done?prolific_id=' + prolific_id + '&participant_id=' + participant_id + '&handle=' + handle, 
		
		data: {
			json: JSON.stringify(data),
			prolific_id: prolific_id,
			handle: handle,
			participant_id: participant_id,
			bonus: scoreinnovelar
		},
		dataType: 'json', 
		//success: function(){
		//}// write the result to javascript console
		success: function(output) { console.log(output); } // write the result to javascript console
	});
	return false
}

function save_datatask(data,prolific_id,participant_id,handle){
	
for (i = 0; i < data.length; i++) {
	delete data[i].internal_chunk_id;
	delete data[i].trial_index_global;
	delete data[i].trial_type;
	}
	
	$.ajax({
		type: "POST",
	    async: false,
		cache: false,
// 		url: 'http://localhost:5000/taskdone?prolific_id=' + prolific_id + '&participant_id=' + participant_id + '&handle=' + handle, 
		url: 'https://api-brainexp.osc-fr1.scalingo.io/taskdone?prolific_id=' + prolific_id + '&participant_id=' + participant_id + '&handle=' + handle, 

		data: {
			json: JSON.stringify(data),
			prolific_id: prolific_id,
			handle: handle,
			participant_id: participant_id,
		},
		dataType: 'json', 
		//success: function(){
		//}// write the result to javascript console
		success: function(output) { console.log(output); } // write the result to javascript console
	});
	return false
}
