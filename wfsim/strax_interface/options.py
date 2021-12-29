
import strax

FAX_OPTIONS = [
    strax.Option('s1_model_type', default='simple'),
    strax.Option('s2_luminescence_model', default='garfield'),
    strax.Option('enable_gas_gap_warping', default=True),
    strax.Option('enable_pmt_afterpulses', default=True),
    strax.Option('enable_electron_afterpulses', default=False),
    strax.Option('enable_noise', default=True),
    strax.Option('field_distortion_on', default=False),
    strax.Option('field_distortion_model', default='none'),
    strax.Option('enable_field_dependencies', default={'survival_probability_map': True, 'drift_speed_map': False, 'diffusion_longitudinal_map': False, 'diffusion_transverse_map': False}),
    strax.Option('url_base', default='https://raw.githubusercontent.com/XENONnT/private_nt_aux_files/master/sim_files'),
    strax.Option('photon_area_distribution', default='XENONnT_spe_distributions_20210713.csv'),
    strax.Option('s1_pattern_map', default='XENONnT_s1_xyz_patterns_LCE_corrected_qes_MCva43fa9b_wires.pkl'),
    strax.Option('s2_pattern_map', default='XENONnT_s2_xy_patterns_LCE_corrected_qes_MCva43fa9b_wires.pkl'),
    strax.Option('s1_lce_correction_map', default=False),
    strax.Option('s2_correction_map', default=False),
    strax.Option('photon_ap_cdfs', default='XENONnT_pmt_afterpulse_config_012605.json.gz'),
    strax.Option('s2_luminescence', default='XENONnT_GARFIELD_B1d5n_C30n_G1n_A6d5p_T1d5n_PMTs1d5n_FSR0d95n.npz'),
    strax.Option('gas_gap_map', default='gas_gap_warping_map_January_2021.pkl'),
    strax.Option('field_dependencies_map', default='field_dependent_radius_depth_maps_B1d5n_C30n_G1n_A6d5p_T1d5n_PMTs1d5n_FSR0d95n.json.gz'),
    strax.Option('temperature', default=177.45),
    strax.Option('pressure', default=1.210852812592475e+18),
    strax.Option('lxe_dielectric_constant', default=1.874),
    strax.Option('tpc_length', default=148.6515),
    strax.Option('tpc_radius', default=66.4),
    strax.Option('anode_wire_radius', default=0.0108),
    strax.Option('anode_field_domination_distance', default=0.089),
    strax.Option('elr_gas_gap_length', default=0.416),
    strax.Option('gate_to_anode_distance', default=0.7888),
    strax.Option('drift_field', default=200.0),
    strax.Option('anode_voltage', default=7500.0),
    strax.Option('diffusion_constant_longitudinal', default=2.439e-08),
    strax.Option('diffusion_constant_transverse', default=5.634e-08),
    strax.Option('drift_time_gate', default=3400.0),
    strax.Option('drift_velocity_liquid', default=0.000155),
    strax.Option('singlet_fraction_gas', default=0.35),
    strax.Option('singlet_lifetime_gas', default=5.88),
    strax.Option('singlet_lifetime_liquid', default=3.1),
    strax.Option('triplet_lifetime_gas', default=149.0),
    strax.Option('triplet_lifetime_liquid', default=24.0),
    strax.Option('s1_ER_alpha_singlet_fraction', default=0.7368421052631579),
    strax.Option('s1_ER_primary_singlet_fraction', default=0.1452991452991453),
    strax.Option('s1_ER_recombination_fraction', default=0.9),
    strax.Option('s1_ER_recombination_time', default=4.276062489602044),
    strax.Option('s1_ER_secondary_singlet_fraction', default=0.4444444444444444),
    strax.Option('s1_NR_singlet_fraction', default=0.8863636363636364),
    strax.Option('maximum_recombination_time', default=50.0),
    strax.Option('s1_decay_spread', default=13),
    strax.Option('s1_decay_time', default=58.02),
    strax.Option('s1_detection_efficiency', default=1.0),
    strax.Option('s2_mean_area_fraction_top', default=-1),
    strax.Option('s2_aft_sigma', default=0.0118),
    strax.Option('s2_aft_skewness', default=-1.433),
    strax.Option('s2_secondary_sc_gain', default=42.64),
    strax.Option('s2_time_spread', default=78.3),
    strax.Option('electron_extraction_yield', default=0.96),
    strax.Option('electron_lifetime_liquid', default=4500000.0),
    strax.Option('electron_trapping_time', default=185.0),
    strax.Option('gas_drift_velocity_slope', default=5400000000000.0),
    strax.Option('p_double_pe_emision', default=0.219),
    strax.Option('pe_pulse_ts', default=[-13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195]),
    strax.Option('pe_pulse_ys', default=[5.877972164179458e-09, 8.655525785456122e-08, 9.494125588317938e-07, 7.896805563760717e-06, 5.0878565098147255e-05, 0.00025904060183682944, 0.0010546866894903517, 0.0034372690428190844, 0.008918175306240714, 0.018366585294685045, 0.03024293464574896, 0.04070285285992151, 0.04650274440945783, 0.04738821191801888, 0.045269280688785586, 0.0420583181746971, 0.03873509136879648, 0.035604682980707264, 0.03271708669859928, 0.03006262425253816, 0.027623450572224897, 0.025382178597567896, 0.023322755583582648, 0.021430427093330644, 0.019691635654062734, 0.018093923795527204, 0.016625844803847056, 0.01527688071229399, 0.014037366945928706, 0.012898423080313378, 0.0117226134274469, 0.010654620425448081, 0.007486532911462879, 0.007122986413393814, 0.006759439915324416, 0.0063958934172549066, 0.006032346919185841, 0.005668800421116332, 0.005305253923046934, 0.004954040729682673, 0.004615160841022549, 0.004498280437047894, 0.004381400033073238, 0.004264519629098583, 0.004147639225123928, 0.004030758821149161, 0.003913878417174506, 0.0037969980131998507, 0.0036801176092253066, 0.0035661831429826276, 0.0034551946144725913, 0.0033972329651430124, 0.003339271315813323, 0.003281309666483744, 0.0032233480171541657, 0.003165386367824587, 0.0031074247184950084, 0.0030494630691652075, 0.002991501419835629, 0.0029345925847569037, 0.002878736563928587, 0.002841831199613188, 0.002804925835297788, 0.0027680204709823884, 0.0027311151066669887, 0.0026942097423514784, 0.0026573043780361897, 0.002620399013720679, 0.002583493649405279, 0.0025470331080403733, 0.0025110173896258497, 0.002483008484319546, 0.0024549995790133527, 0.0024269906737071595, 0.002398981768400855, 0.002370972863094662, 0.0023429639577884688, 0.0023149550524821645, 0.0022869461471758602, 0.0022592201366423946, 0.002231777020881435, 0.0022094260110277998, 0.0021870750011742757, 0.0021647239913207515, 0.002142372981467338, 0.002120021971613703, 0.0020976709617601787, 0.0020753199519066546, 0.002052968942053241, 0.0020307543953674546, 0.00200867631184985, 0.001989054565354189, 0.001969432818858306, 0.0019498110723626448, 0.0019301893258668727, 0.0019105675793713226, 0.0018909458328754394, 0.0018713240863797783, 0.0018517023398840063, 0.0018323263223003487, 0.0018131960336284728, 0.0017984888653722166, 0.0017837816971160714, 0.0017690745288597041, 0.001754367360603559, 0.0017396601923473027, 0.0017249530240910464, 0.0017102458558346792, 0.001695538687578423, 0.0016813056397601814, 0.0016675467123799547, 0.0016623219528827716, 0.0016570971933854775, 0.0016518724338885165, 0.0016466476743912226, 0.0016414229148939284, 0.0016361981553968564, 0.0016309733958997843, 0.0016257486364023791, 0.0016202321178094528, 0.00161442384012045, 0.0016033638987052918, 0.001592303957290245, 0.0015812440158751977, 0.0015701840744600396, 0.0015591241330449924, 0.0015480641916298342, 0.001537004250214787, 0.0015259443087995179, 0.0015148109383005546, 0.0015036041387176751, 0.001491075615624526, 0.0014785470925315991, 0.001466018569438339, 0.001453490046345301, 0.001440961523252152, 0.0014284330001590028, 0.0014159044770659648, 0.0014033759539728158, 0.0013911025358676267, 0.0013790842227502866, 0.0013716577994147816, 0.0013642313760793877, 0.0013568049527439938, 0.001349378529408378, 0.0013419521060730952, 0.0013345256827375902, 0.0013270992594020853, 0.0013196728360666916, 0.0013122629141418373, 0.001304869493627745, 0.0012977730985050332, 0.0012906767033823215, 0.001283580308259388, 0.0012764839131367872, 0.0012693875180140755, 0.0012622911228913638, 0.001255194727768541, 0.0012480983326459403, 0.0012409999123474602, 0.0012338994668731004, 0.0012267625682346867, 0.001219625669596495, 0.0012124887709579703, 0.0012053518723195566, 0.0011982149736811428, 0.0011910780750428401, 0.0011839411764043154, 0.0011768042777659017, 0.0011693420067777262, 0.0011615543634395673, 0.0011479100178038103, 0.0011342656721679426, 0.0011206213265321859, 0.00110697698089654, 0.0010933326352606722, 0.0010796882896250263, 0.0010660439439892696, 0.0010523995983534019, 0.0010394190161775144, 0.0010271021974616074, 0.0010267331210240156, 0.001026364044586091, 0.0010259949681484994, 0.0010256258917104636, 0.001025256815272983, 0.0010248877388350584, 0.0010245186623973556, 0.001024149585959653, 0.0010225269485754907, 0.0010196507502449798, 0.0009942104548798607, 0.0009687701595146309, 0.0009433298641495118, 0.0009178895687842819, 0.000892449273419274, 0.000867008978054155, 0.000841568682688814, 0.0008161283873238061, 0.0007904692274874684, 0.0007645912031799121, 0.0007347736183906416, 0.0007049560336012601, 0.0006751384488119896, 0.0006453208640227192, 0.0006155032792334486, 0.0005856856944440671, 0.0005558681096547966, 0.0005260505248655261]),
    strax.Option('pmt_ap_modifier', default=1),
    strax.Option('pmt_ap_t_modifier', default=270),
    strax.Option('pmt_pulse_time_rounding', default=1.0),
    strax.Option('pmt_transit_time_mean', default=46.0),
    strax.Option('pmt_transit_time_spread', default=9.0),
    strax.Option('photoelectric_modifier', default=1),
    strax.Option('photoelectric_p', default=0.001),
    strax.Option('photoelectric_t_center', default=-800),
    strax.Option('photoelectric_t_spread', default=250),
    strax.Option('photoionization_modifier', default=1),
    strax.Option('sample_duration', default=10),
    strax.Option('samples_after_pulse_center', default=20),
    strax.Option('samples_before_pulse_center', default=2),
    strax.Option('samples_to_store_after', default=50),
    strax.Option('samples_to_store_before', default=50),
    strax.Option('pmt_circuit_load_resistor', default=8.010882825e-09),
    strax.Option('external_amplification', default=10),
    strax.Option('high_energy_deamplification_factor', default=0.05),
    strax.Option('trigger_window', default=50),
    strax.Option('digitizer_bits', default=14),
    strax.Option('digitizer_reference_baseline', default=16000),
    strax.Option('digitizer_voltage_range', default=2.25),
    strax.Option('special_thresholds', default={'260': 60, '313': 25, '343': 1000, '355': 25, '37': 255, '376': 1000, '393': 60, '405': 1000, '416': 25, '434': 60, '448': 1000, '453': 60, '500': 10, '501': 10, '502': 10, '503': 10, '504': 10, '505': 10, '506': 10, '507': 10, '508': 10, '509': 10, '510': 10, '511': 10, '512': 10, '513': 10, '514': 10, '515': 10, '516': 10, '517': 10, '518': 10, '519': 10, '520': 10, '521': 10, '522': 10, '523': 10, '524': 10, '525': 10, '526': 10, '527': 10, '528': 10, '529': 10, '530': 10, '531': 10, '532': 10, '533': 10, '534': 10, '535': 10, '536': 10, '537': 10, '538': 10, '539': 10, '540': 10, '541': 10, '542': 10, '543': 10, '544': 10, '545': 10, '546': 10, '547': 10, '548': 10, '549': 10, '550': 10, '551': 10, '552': 10, '553': 10, '554': 10, '555': 10, '556': 10, '557': 10, '558': 10, '559': 10, '560': 10, '561': 10, '562': 10, '563': 10, '564': 10, '565': 10, '566': 10, '567': 10, '568': 10, '569': 10, '570': 10, '571': 10, '572': 10, '573': 10, '574': 10, '575': 10, '576': 10, '577': 10, '578': 10, '579': 10, '580': 10, '581': 10, '582': 10, '583': 10, '584': 10, '585': 10, '586': 10, '587': 10, '588': 10, '589': 10, '590': 10, '591': 10, '592': 10, '593': 10, '594': 10, '595': 10, '596': 10, '597': 10, '598': 10, '599': 10, '600': 10, '601': 10, '602': 10, '603': 10, '604': 10, '605': 10, '606': 10, '607': 10, '608': 10, '609': 10, '610': 10, '611': 10, '612': 10, '613': 10, '614': 10, '615': 10, '616': 10, '617': 10, '618': 10, '619': 10, '620': 10, '621': 10, '622': 10, '623': 10, '624': 10, '625': 10, '626': 10, '627': 10, '628': 10, '629': 10, '630': 10, '631': 10, '632': 10, '633': 10, '634': 10, '635': 10, '636': 10, '637': 10, '638': 10, '639': 10, '640': 10, '641': 10, '642': 10, '643': 10, '644': 10, '645': 10, '646': 10, '647': 10, '648': 10, '649': 10, '650': 10, '651': 10, '652': 10, '653': 10, '654': 10, '655': 10, '656': 10, '657': 10, '658': 10, '659': 10, '660': 10, '661': 10, '662': 10, '663': 10, '664': 10, '665': 10, '666': 10, '667': 10, '668': 10, '669': 10, '670': 10, '671': 10, '672': 10, '673': 10, '674': 10, '675': 10, '676': 10, '677': 10, '678': 10, '679': 10, '680': 10, '681': 10, '682': 10, '683': 10, '684': 10, '685': 10, '686': 10, '687': 10, '688': 10, '689': 10, '690': 10, '691': 10, '692': 10, '693': 10, '694': 10, '695': 10, '696': 10, '697': 10, '698': 10, '699': 10, '700': 10, '701': 10, '702': 10, '703': 10, '704': 10, '705': 10, '706': 10, '707': 10, '708': 10, '709': 10, '710': 10, '711': 10, '712': 10, '713': 10, '714': 10, '715': 10, '716': 10, '717': 10, '718': 10, '719': 10, '720': 10, '721': 10, '722': 10, '723': 10, '724': 10, '725': 10, '726': 10, '727': 10, '728': 10, '729': 10, '730': 10, '731': 10, '732': 10, '733': 10, '734': 10, '735': 10, '736': 10, '737': 10, '738': 10, '739': 10, '740': 10, '741': 10, '742': 10, '743': 10, '744': 10, '745': 10, '746': 10, '747': 10, '748': 10, '749': 10, '750': 10, '751': 10, '752': 10, '801': 30, '802': 30, '803': 30, '804': 30, '805': 30, '806': 30, '807': 30, '999': 255}),
    strax.Option('zle_threshold', default=15),
]