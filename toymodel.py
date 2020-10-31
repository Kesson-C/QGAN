import qiskit
import numpy as np

backend = qiskit.BasicAer.get_backend('qasm_simulator')

NUM_SHOTS = 10000

def get_probability_distribution(counts):
    output_distr = [v / NUM_SHOTS for v in counts.values()]
    if len(output_distr) == 1:
        output_distr.append(0)
    return output_distr

def generator(w,qc,n):
	for i in range(n):
	qc.h(0)
	qc.rx(w[0],0)
	qc.rx(w[1],1)
	qc.ry(w[2],0)
	qc.ry(w[3],1)
	qc.rz(w[4],0)
	qc.rz(w[5],1)
	qc.cx(0,1)
	qc.rx(w[6],0)
	qc.ry(w[7],0)
	qc.rz(w[8],0)
	qc.measure([0],[0])

#def discriminator(w,qc):
#	qc.h(0)
#	qc.rx(w[0],0)
#	qc.rx(w[1],2)
#	qc.ry(w[2],0)
#	qc.ry(w[3],2)
#	qc.rz(w[4],0)
#	qc.rz(w[5],2)
#	qc.cx(0,2)
#	qc.rx(w[6],2)
#	qc.ry(w[7],2)
#	qc.rz(w[8],2)
#	qc.measure([2],[2])

def real_disc(angels,w,qc):
	real(angels,qc)
	discriminator(w,qc)
	prob = get_probability_distribution(qiskit.execute(qc,backend,shots=NUM_SHOTS).result().get_counts())
	expv = -1*prob[0]+prob[1]
	return expv

def gen_disc(gw,dw,qc):
	generator(gw,qc)
	discriminator(dw,qc)
	prob = get_probability_distribution(qiskit.execute(qc,backend,shots=NUM_SHOTS).result().get_counts())
	expv = -1*prob[0]+prob[1]
	return expv

def prob_real_true(angels,dw):		
	tout = real_disc(angels,dw)
	prob = (tout+1)/2
	return prob

def prob_fake_true(gw,dw):		
	tout = gen_disc(gw,dw)
	prob = (tout+1)/2
	return prob

def disc_cost(angels,gw,dw):
	cost = prob_fake_ture(gw,dw) - prob_real_true(angles,dw)
	return cost

def gen_cost(gw):
	return -prob_fake_true(gw,dw)

qc_real = qiskit.QuanrumCircuit(1,1)
qc = qiskit.QuantumCircuit(2,2)
angels = [0.3 0.5 0.4]



