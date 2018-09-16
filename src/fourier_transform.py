import numpy as np
import scipy.fftpack

def fourier(audio, chunk_size=20000):
	chunks = [audio[i:i+chunk_size] for i in range(len(audio)//chunk_size+1)]
	return [np.fft.rfft(chunk) for chunk in chunks] 

if __name__ == '__main__':
	audio = [-0.0054060705, -0.0037189426, -0.004261127, -0.00513171, -0.0053035356, -0.0054353066, -0.0057619405, -0.006607028, -0.003849341, -0.0046216114, -0.0046287253, -0.0037470227, -0.0027607263, -0.0033051337, -0.0034881292, -0.0030559944, -0.005130441, -0.0038939104, -0.005947785, -0.006310129, -0.007614142, -0.009229978, -0.009152191, -0.009259527, -0.01031017, -0.010268288, -0.009408698, -0.011965619, -0.010486588, -0.01019477, -0.009950135, -0.008703522, -0.008465822, -0.0074876174, -0.005539734, -0.004141709, -0.002657274, 0.0009993616, 0.0014471576, 0.0037164136, 0.005063167, 0.0049899817, 0.0059475857, 0.0061310865, 0.005980574, 0.0043248176, 0.0046801292, 0.0043064966, 0.0030335377, 0.0037612813, 0.0024627247, 0.0018753534, 0.0013491296, 0.0007458924, 0.0015026223, 0.0012546114, 0.002137328, 0.0015166044, 0.000986688, 0.0014715997, 0.00033963402, 0.00033425455, 0.0006075947, -0.0027581642, -0.00059054815, -0.0014857581, -0.0034936827, -0.0016285587, -0.003720587, -0.0021468713, -0.0024207323, -0.0025618265, -0.0011926901, -2.0162177e-05, 0.00058904535, 0.0038822787, 0.0016835369, 0.001406788, 0.0033967607, 0.0015699199, 0.0031488168, 0.0040543783, 0.0075092264, 0.0080073755, 0.009702453, 0.011325919, 0.010993162, 0.012029036, 0.011243519, 0.011365677, 0.0119241355, 0.010668589, 0.010522503, 0.010083979, 0.010329736, 0.011431361, 0.010340921, 0.010791531, 0.010822334, 0.010298635, 0.009247616, 0.008574242, 0.009199256, 0.007363872, 0.00832905, 0.008552488, 0.007956658, 0.006887942, 0.007840529, 0.006307367, 0.0040701022, 0.0037448606, 0.001991422, 0.0016559702, 0.002165989, 0.0034050194, 0.004323507, 0.0062620156, 0.005421329, 0.008107628, 0.0088810455, 0.008637135, 0.008900451, 0.009467494, 0.00791402, 0.007854295, 0.009201164, 0.007208329, 0.008201276, 0.007239469, 0.0068644322, 0.0065500634, 0.0075084358, 0.00788365, 0.0072661326, 0.009269969, 0.010721365, 0.010651355, 0.014287184, 0.014718676, 0.013562622, 0.012728525, 0.00883027, 0.010353761, 0.005660095, 0.0043435935, 0.004067171, 0.0023620152, 0.003498676, 0.00089865626, 0.0045701037, 0.0025030712, 0.002305648, 0.0046034018, 0.0020020506, 0.0020209665, 0.0014638357, 0.0012169724, 0.00055882183, 0.0020760067, 0.0012383715, 0.0023194358, 0.0024663194, 0.00041194973, 0.0015594868, 9.278235e-05, 0.00011504117, 0.0017049416, 0.0019511189, 0.0019305549, 0.0012526654, 0.0014724076, 0.0027204535, -0.0006670042, 0.0009814401, 0.0014903974, -0.00061671564, 0.00076210854, 0.00036017032, 0.0012650167, 0.00073035737, 0.00023123826, 0.0023615602, 0.0023887227, -0.0003295081, 0.0020590292, 0.00053152425, -0.0024522485, -0.00052649534, -0.0040817345, -0.0027625812, -0.0032464191, -0.006639793, -0.0070031993, -0.0057591773, -0.006917395, -0.010367101, -0.008765423, -0.01018753, -0.011451824, -0.008933101, -0.011209056, -0.012875685, -0.011008664, -0.013436143, -0.012422593, -0.014689534, -0.015587011, -0.0137661, -0.0143424, -0.012015567, -0.010941186, -0.010268144, -0.009893796, -0.008999281, -0.009297867, -0.009591819, -0.008801209, -0.008366686, -0.00686301, -0.006688685, -0.0069042807, -0.006585201, -0.0054789344, -0.006449128, -0.006239265, -0.0045855246, -0.004385482, -0.0036277405, -0.0040909466, -0.0018589917, -0.0023793594, -0.002573855, 0.00022799267, -0.00036824518, 0.00012172661, 0.00015125667, 0.00074858195, 0.0011119404, 0.00012353256, 0.00030895538, 0.00067949505, 0.0021482925, -0.0013270664, -0.000517394, 0.0015371533, -0.0013508616, -0.0019938622, -0.0020162635, -0.0016330334, -0.0017298001, -0.0032862, -0.0015218774, -0.0021929003, -0.002980624, -0.0016194896, -0.0018211394, 0.0014352152, 0.001378674, 0.0029446078, 0.004165362, 0.004151154, 0.0054509277, 0.0030675456, 0.0011548582, 0.001090861, 0.00048915675, 0.0005935698, 0.00127047, 0.0007594805, 0.0028463707, 0.004522893, 0.005530686, 0.005808226, 0.0059571234, 0.0046253703, 0.0046091974, 0.0054222075, 0.0014816823, 0.0024182124, 0.002697067, 0.0007540685, 0.0013051188, 0.0003861189, 0.0013138361, 0.0010957865, 0.0001855437, 0.0012597658, 0.0020730402, 0.004259562, 0.001690813, 0.0027625845, 0.0018560793, 0.0023157296, 0.0022061514, -2.474751e-05, 0.0037138152, 0.0019771813, 0.0036996936, 0.004805983, 0.0046888944, 0.0054156766, 0.0043109427, 0.004252797, 0.0051115965, 0.0046660034, 0.003648827, 0.004977536, 0.0029881252]
	fourier(audio)



