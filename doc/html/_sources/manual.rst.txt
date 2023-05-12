Installation
=====================================================
The program is written with Python. Thus, the program is executable in Windows platform or Linux platform.  Please make sure that you install Python 3 including **numpy, matplotlib, scipy, csv, copy, datetime, sys and os package** on your computer.

To download the project, please install git in your computer, and type the following command in git bash environment.

.. code-block:: console

	git clone https://github.com/mingchunNTU/Batch_Crystallization_v1.git
	
Important Script
=======================================================
There're four important scripts that provide different functions. There's a section that defines adjustable parameters in the beginning of the source code. The acceptable option is explained in comment section. 

* src/run.py: execute the simulation, and output the trajectory and product CSD
* src/plot_CSD.py: plot the product CSD
* src/plot_trajectory.py: plot the trajectory during crystallization
* src/transform_CSD.py: transform the product CSD from number fraction to volume fraction

File Structure
==========================================================
To avoid editing the source code frequently, the physical properties and operating condition are defined in separated files from the main script. You can define the directory that contains these setting files using a parameters setting_dir in the source code. You can modify the examples in src/examples/KNO3 to fit your need. The kinetic parameters used in the example are from the work of Chung et al. (1). The description of the files are shown below.

* operating_condition.csv: the operating condition of the crystallizer
* physical_property.csv: the crystal property and crystallization kinetic parameters
* Result/CSD.csv: the simulated crystal size distriubtion
* Result/trajectory.csv: the trajectory during batch crystallization


Ref: (1) Chung, S. H.; Ma, D. L.; Braatz, R. D. Optimal Seeding in Batch Crystallization. The Canadian journal of chemical engineering 1999, 77 (3), 590–596.

Simulation of Crystallization
====================================================
Please edit the operating_condition.csv and physical_property.csv according to the system you studied. The crystallization kinetic parameter, solubility and crystal property are stored in physical_property.csv file. The operation parameters such as seed condition and cooling trajectory are stored in operation.csv file.

The form of solubility in crystallization_simulator is shown as

.. math::

	Csat=A+B*T+C*T^2 

T is in unit of :math:`^oC` and Csat is in unit of g solute/L solvent

The unit of solubility, seed loading and crystal density should be the same because of the mass balance equation. The time and length unit of kg and kb should be consistent because of moment equation. The birth rate used in the simulation is normallized by the solvent volume. Thus, the third moment is dimensionless. 

The seed CSD is assumed to be parabolic form.

.. math:: 

	f(r)=A*r_0(1+w)(1-w)

for :math:`r_0(1+w)>r>r_0(1-w)`

The temperature trajectory is defined in a polynomial form.

.. math::

	T(t)=T_i-(T_i-T_e)*(\frac{t}{batch time})^j
	
T is temperature. Ti is initial temperature. Te is end temperature. t is time. j is the order of the trajectory 

After specifying all the parameters, please edit setting_dir in the run.py and execute the program. After simulation finished, you can use plot_CSD.py or plot_trajectory.py scripts to visuallize the results. If a volumbe based CSD is prefered, you can run transform_CSD.py first and then execute plot_CSD.py.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`