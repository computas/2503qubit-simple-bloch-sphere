from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt
import numpy as np


qc = QuantumCircuit(1)
qc.ry(np.pi / 4, 0)  


backend = Aer.get_backend('statevector_simulator')
transpiled_qc = transpile(qc, backend)
job = backend.run(transpiled_qc)
result = job.result()
statevector = result.get_statevector()


fig = plot_bloch_multivector(statevector)


plt.title(r"$\alpha = \sqrt{\frac{2 + \sqrt{2}}{4}}, \quad \beta = \sqrt{\frac{2 - \sqrt{2}}{4}}$")

plt.show()
