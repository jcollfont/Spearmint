function [c, f, output] = neuralNetWrapper( dropout_In,dropout_Hi,momentum, weightDecay, maxWeight)

	paramsString = sprintf('\''-dIn\'' %f \''-dHi\'' %f \''-mo\'' %f \''-wD\'' %f \''-wM\'' %f', dropout_In,dropout_Hi,momentum, weightDecay, maxWeight);
	
	commandString = 'python MINST_keras_remote.py';
	
	fullCommand = sprintf('%s %s', commandString, paramsString);
	
	[status,cmdout] = system(fullCommand);
	
	splitOut = strsplit(cmdout, '\n');
	
	output = splitOut{end-1};
	A =sscanf(output,'{\"c\": %f, \"f\": [%f, %f]}');
	
	c = A(1);
	f = A(end);

end
