/*(
~oscServo = OSCdef(\oscTest,
	    {
		         | ... msg |


		         msg[0][1].asString.postln;
		},'/motion'
)
)


*/


~oscServo = OSCdef(\oscTest,
	{
		| ... msg |


		msg[0][1].asString.postln;

		fork{
			[

				//1

				if (msg[0][1]==1){[

				[	BellPat.pattern1(\pat1, ip: "127.0.0.1", rep: 1, angleIn:0.rand, angleOut:90.rand, sleep:0.25.rand, waitTime:1.rand);,
					BellPat.pattern2(\pat2, ip: "127.0.0.1", st:"0", rep:1, angleIn:"0", angleOut:"90", bet:0.125, waitTime:0.25);
				].choose;
"Hello".postln;
				]}{};
				if (msg[0][1]==0){[
					//Planets.grains(\vasilis, \x2, sensz:\z2, vol: 0.005, gate:0, sndbuf:'wavesSeamono'.bufnum);
					//\grains.stop;
"Bye".postln;


				]};
			]}
	},
				'/motion'
);






			//BellPat.pattern1(\pat1, ip: "192.168.5.110", rep: 1, angleIn:0, angleOut:45, sleep:0.25, waitTime:1);
			//BellPat.pattern2(\pat2, ip: "192.168.5.110", st:"0", rep:1, angleIn:"0", angleOut:"90", bet:0.125, waitTime:0.25);
