BellPat{

	classvar <>server;
classvar <addr;


	*pattern1{|name, ip="192.168.1.4", rep = 1,
		first="/servo1", second="/servo2", third="/servo3", fourth="/servo4",
		angleIn = "0", angleOut = "90",
		sleep = 0.5, waitTime=1|

addr = NetAddr(ip, 5005);// rpi machine


fork{
rep.do{
[	addr.sendMsg(first, angleIn.asString);
	sleep.wait;
	addr.sendMsg(second, angleIn.asString);
	sleep.wait;
	addr.sendMsg(third, angleIn.asString);
	sleep.wait;
	addr.sendMsg(fourth, angleIn.asString);
    waitTime.wait;
	addr.sendMsg(fourth, angleOut.asString);
	sleep.wait;
	addr.sendMsg(third, angleOut.asString);
	sleep.wait;
    addr.sendMsg(second, angleOut.asString);
	sleep.wait;
    addr.sendMsg(first, angleOut.asString);
	sleep.wait;

				].choose;
				waitTime.wait;

			};
};


	}

	*pattern2{|name, ip="192.168.1.4", st="0", rep = 1, first="/servo1", second="/servo2", third="/servo3", fourth="/servo4", angleIn="0", angleOut="90", bet = 0.5, waitTime = 1|

addr = NetAddr(ip, 5005);// rpi machine


		Routine({

			var state = st;
    rep.do { |i|
		state.postln;
				state = (state == st).if { angleOut } { angleIn };
        //sendOSC.sendMsg("/number", state.asInteger);
		        addr.sendMsg(first, state.asInteger);
				                bet.wait;
		        addr.sendMsg(second, state.asInteger);
								bet.wait;

		        addr.sendMsg(third, state.asInteger);
								bet.wait;

		        addr.sendMsg(fourth, state.asInteger);
								bet.wait;


		     //   sendOSC.sendMsg("/filter2", state.asInteger);

        waitTime.wait;
    };
}).play;
	}

	*pattern3{|name, ip="192.168.1.4", rep=1, first="/servo1", second="/servo2", third="/servo3", fourth="/servo4", angleIn="0", angleOut="90", bet = 0.5, waitTime = 1|

		addr = NetAddr(ip, 5005);

		fork{

			rep.do{
	addr.sendMsg(first, angleIn.asString);

			};

		}

	}




	}








