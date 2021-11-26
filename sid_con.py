import math

class Resource:

	def __init__(self, resource, donation = False):
		resource = resource.lower()
		if resource == "white":
			self.value = 1
			self.id = 1
		elif resource == "green":
			self.value = 1
			self.id = 2
		elif resource == "brown":
			self.value = 1
			self.id = 3
		elif resource == "ship":
			self.value = 1
			self.id = 4
		elif resource == "blue":
			self.value = 2
			self.id = 5
		elif resource == "yellow":
			self.value = 2
			self.id = 6
		elif resource == "black":
			self.value = 2
			self.id = 7
		elif resource == "octagon":
			self.value = 3
			self.id = 8
		elif resource == "point":
			self.value = 3
			self.id = 9
		else:
			raise("Value Error")

		self.resource = resource
		self.donation = donation

	def __eq__(self, other):
		if isinstance(other, Resource):
			return self.id == other.id and self.donation == other.donation
		return False


class Tech:
	def __init__(self, tech_id, resource, points):
		self.resource = resource
		self.points = points



class Colony:

	def __init__(self, resource, planet_res, upgrade_output, upgrade_planet_res):
		planet_res = planet_res.lower()
		if planet_res == "ice":
			self.planet_res = planet_res
		elif planet_res == "desert":
			self.planet_res = planet_res
		elif planet_res == "jungle":
			self.planet_res = planet_res
		elif planet_res == "ocean":
			self.planet_res = planet_res
		else:
			raise ValueError("This is not a planet type")

		upgrade_planet_res = upgrade_planet_res.lower()
		if upgrade_planet_res == "ice":
			self.upgrade_planet_res = upgrade_planet_res
		elif upgrade_planet_res == "desert":
			self.upgrade_planet_res = upgrade_planet_res
		elif upgrade_planet_res == "jungle":
			self.upgrade_planet_res = upgrade_planet_res
		elif upgrade_planet_res == "ocean":
			self.upgrade_planet_res = upgrade_planet_res
		else:
			raise ValueError("This is not a planet type")

		self.resource = resource
		self.upgrade_output = upgrade_output
		self.upgraded = False

	def upgrade():
		if not self.upgraded:
			self.upgraded = True
			self.resource = self.upgrade_output
			self.planet_res = self.upgrade_planet_res
			self.upgrade_output = None
			self.upgrade_planet_res = None
		else:
			raise ValueError("Converter already upgraded")


class Converter:
	def __init__(self, input_res, output_res, name, upgrade):
		self.input = input_res
		self.output = output_res
		self.name = name
		self.upgrade = upgrade

	def upgrade():
		self.output.extend(upgrade)


class Hand:
	def __init__(self, resources, converters, colonies, tech):
		self.resources = []
		self.converters = []
		self.colonies = []
		self.tech = []

	def add_resource(self, resource):
		if isinstance(resource, Resource):
			self.resource.append(resource)
		else:
			raise ValueError("Not a resource")

	def add_converter(self, converter):
		if isinstance(converter, Converter):
			self.converters.append(converter)
		else:
			raise ValueError("Not a converter")

	def add_colony(self, colony):
		if isinstance(colony, Colony):
			self.colonies.append(colony)
		else:
			raise ValueError("Not a colony")

	def add_tech(self, tech):
		if isinstance(tech, Tech):
			self.tech.append(tech)
		else:
			raise ValueError("Not a tech")

	def can_run_converter(self, converter):
		required = converter.input
		for resource in self.resources:
			if resource in required:
				required.remove(resource)
		return required == []

	def run_converter(self, converter):
		if can_run_converter(converter):
			for resource in converter.input:
				self.resources.remove(resource)
			for resource in converter.output:
				add_resource(resource)
		else:
			raise ValueError("Not enough resources")


def make_resources(resource, number, donation=False):
	return [Resource(resource,donation=donation) for i in range(number)]

techs = [{
		"name": "Linguistic Analysis",
		"rank": 1
		"resource": (make_resources("green",6),make_resources("black",4)),
		"points": Resource("point"),
		"invent": "Universal Translator"
		},
		{
		"name": "Computational Theoreticans",
		"rank": 1
		"resource": (make_resources("white",6),make_resources("blue",4)),
		"points": Resource("point"),
		"invent": "Quantum Computers"
		},
		{
		"name": "Mechanical Engineers",
		"rank": 1
		"resource": (make_resources("yellow",4),make_resources("octagon",2)),
		"points": Resource("point"),
		"invent": "Nanotechnology"
		},
		{
		"name": "Organic Chemists",
		"rank": 1
		"resource": (make_resources("brown",6),make_resources("blue",4)),
		"points": Resource("point"),
		"invent": "Genetic Engineering"
		},
		{
		"name": "Sociologists",
		"rank": 1
		"resource": (make_resources("white",6),make_resources("black",4)),
		"points": Resource("point"),
		"invent": "Ubiquitous Cultural Repository"
		},
		{
		"name": "Pharmaceutical Scientists",
		"rank": 1
		"resource": (make_resources("green",6),make_resources("octagon",8)),
		"points": Resource("point"),
		"invent": "Clinical Immortality"
		},
		{
		"name": "Nuclear Physicists",
		"rank": 1
		"resource": (make_resources("brown",6),make_resources("yellow",4)),
		"points": Resource("point"),
		"invent": "Atomic Transmutation"
		},
		{
		"name": "Metaethicists",
		"rank": 2
		"resource": (make_resources("yellow",7),make_resources("black",4)),
		"points": make_resources("point",4),
		"invent": "Cross Species Ethical Equality"
		},
		{
		"name": "Gravitic Topologists",
		"rank": 2
		"resource": (make_resources("green",12),make_resources("brown",12)),
		"points": make_resources("point",4),
		"invent": "Singularity Control"
		},
		{
		"name": "Organic Architects",
		"rank": 2
		"resource": (make_resources("yellow",6),make_resources("white",9)),
		"points": make_resources("point",3),
		"invent": "Organic Construction"
		},
		{
		"name": "N-Space Mathematicians",
		"rank": 2
		"resource": (make_resources("blue",8),make_resources("octagon",4)),
		"points": make_resources("point",4),
		"invent": "Hyperspace Mining"
		},
		{
		"name": "Quantum Theoreticans",
		"rank": 2
		"resource": (make_resources("green",9),make_resources("blue",6)),
		"points": make_resources("point",3),
		"invent": "Antimatter Power"
		},
		{
		"name": "Quantum Statisticians",
		"rank": 2
		"resource": (make_resources("white",12),make_resources("octagon",4)),
		"points": make_resources("point",4),
		"invent": "Achronal Analysis"
		},
		{
		"name": "Comparative Physiologists",
		"rank": 2
		"resource": (make_resources("brown",9),make_resources("black",6)),
		"points": make_resources("point",3),
		"invent": "Interspecies Medical Exchange"
		},
		{
		"name": "Interspecies Managers",
		"rank": 3
		"resource": (make_resources("blue",11),make_resources("black",11)),
		"points": make_resources("point",8),
		"invent": "Poly Species Corporations"
		},
		{
		"name": "Memetic Artists",
		"rank": 3
		"resource": (make_resources("brown",18),make_resources("white",18)),
		"points": make_resources("point",9),
		"invent": "Galactic Telecomm Control"
		},
		{
		"name": "Chronophysicists",
		"rank": 3
		"resource": (make_resources("brown",18),make_resources("octagon",6)),
		"points": make_resources("point",9),
		"invent": "Temporal Dilation"
		},
		{
		"name": "Psychohistorians",
		"rank": 3
		"resource": (make_resources("black",12),make_resources("octagon",6)),
		"points": make_resources("point",9),
		"invent": "Social Exodus"
		},
		{
		"name": "Cultural Diffusionologists",
		"rank": 3
		"resource": (make_resources("green",15),make_resources("yellow",10)),
		"points": make_resources("point",7),
		"invent": "Xeno Cultural Exchange"
		},
		{
		"name": "Stellar Architectural Planners",
		"rank": 3
		"resource": (make_resources("blue",14),make_resources("yellow",14)),
		"points": make_resources("point",11),
		"invent": "Megastructures"
		},
		{
		"name": "Subquantum Manipulators",
		"rank": 3
		"resource": (make_resources("white",18),make_resources("green",18)),
		"points": make_resources("point",9),
		"invent": "Matter Generation"
		},
		{
		"name": "Sapience Developers",
		"rank": 4
		"resource": (make_resources("white",21),make_resources("yellow",14),make_resources("black",14)),
		"points": make_resources("point",10),
		"invent": None
		},
		{
		"name": "Recursive Metatheoreticians",
		"rank": 4
		"resource": (make_resources("white",30),make_resources("brown",30),make_resources("black",20)),
		"points": make_resources("point",16),
		"invent": None
		},
		{
		"name": "Cultural Polymorphologists",
		"rank": 4
		"resource": (make_resources("white",18),make_resources("brown",18),make_resources("octagon",6)),
		"points": make_resources("point",8),
		"invent": None
		},
		{
		"name": "Plasma Auxonologists",
		"rank": 4
		"resource": (make_resources("green",24),make_resources("brown",24),make_resources("yellow",16)),
		"points": make_resources("point",12),
		"invent": None
		},
		{
		"name": "Applied Topologists",
		"rank": 4
		"resource": (make_resources("white",30),make_resources("brown",30),make_resources("yellow",20)),
		"points": make_resources("point",16),
		"invent": None
		},
		{
		"name": "Automatic Teleoperators",
		"rank": 4
		"resource": (make_resources("blue",12),make_resources("yellow",12),make_resources("black",12)),
		"points": make_resources("point",8),
		"invent": None
		},
		{
		"name": "In Situ Genetic Editors",
		"rank": 4
		"resource": (make_resources("green",24),make_resources("brown",24),make_resources("black",16)),
		"points": make_resources("point",12),
		"invent": None
		},
		{
		"name": "Chaos Theoreticans",
		"rank": 4
		"resource": (make_resources("green",18),make_resources("yellow",12),make_resources("black",12)),
		"points": make_resources("point",8),
		"invent": None
		},
		{
		"name": "Fractal Microbiologists",
		"rank": 4
		"resource": (make_resources("white",21),make_resources("green",21),make_resources("blue",14)),
		"points": make_resources("point",10),
		"invent": None
		},
		{
		"name": "Psychohistorial Ethicists",
		"rank": 4
		"resource": (make_resources("white",27),make_resources("green",27),make_resources("black",18)),
		"points": make_resources("point",14),
		"invent": None
		},
		{
		"name": "Mesoscale Geoengineers",
		"rank": 4
		"resource": (make_resources("brown",27),make_resources("yellow",18),make_resources("octagon",9)),
		"points": make_resources("point",14),
		"invent": None
		},
		{
		"name": "Tachyon Astrotechnicians",
		"rank": 4
		"resource": (make_resources("green",30),make_resources("yellow",20),make_resources("blue",20)),
		"points": make_resources("point",16),
		"invent": None
		},
		{
		"name": "Interphasal Theoreticans",
		"rank": 4
		"resource": (make_resources("brown",24),make_resources("green",24),make_resources("octagon",8)),
		"points": make_resources("point",12),
		"invent": None
		},
		{
		"name": "Metacognitive Ecologists",
		"rank": 4
		"resource": (make_resources("green",30),make_resources("blue",20),make_resources("octagon",10)),
		"points": make_resources("point",16),
		"invent": None
		},
		{
		"name": "Singularity Control Technicians",
		"rank": 4
		"resource": (make_resources("black",20),make_resources("blue",20),make_resources("octagon",10)),
		"points": make_resources("point",16),
		"invent": None
		},
		{
		"name": "Reconstructive Paleobotanists",
		"rank": 4
		"resource": (make_resources("green",21),make_resources("white",21),make_resources("octagon",7)),
		"points": make_resources("point",16),
		"invent": None
		},
		{
		"name": "Marcoscale Biophysicists",
		"rank": 4
		"resource": (make_resources("brown",27),make_resources("black",18),make_resources("blue",18)),
		"points": make_resources("point",14),
		"invent": None
		},
		{
		"name": "Abiotic Pathologists",
		"rank": 4
		"resource": (make_resources("white",24),make_resources("yellow",16),make_resources("octagon",8)),
		"points": make_resources("point",12),
		"invent": None
		},
		{
		"name": "Oceanographic Biotechnicians",
		"rank": 4
		"resource": (make_resources("brown",18),make_resources("blue",12),make_resources("octagon",6)),
		"points": make_resources("point",8),
		"invent": None
		},
		{
		"name": "Stellar Plasma Flow Engineers",
		"rank": 4
		"resource": (make_resources("brown",21),make_resources("blue",14),make_resources("black",14)),
		"points": make_resources("point",10),
		"invent": None
		}]

faderan_converters = [{
		"name": "Universal Translator",
		"input": make_resources("white",3),
		"output": [Resource("point"), Resource("black" donation=True)],
		"upgrade": [Resource("white" donation=True),Resource("brown" donation=True)]
		},
		{
		"name": "Quantum Computers",
		"input": make_resources("black",2),
		"output": [Resource("blue"),Resource("yellow"),Resource("brown")],
		"upgrade": [Resource("brown")]
		},
		{
		"name": "Nanotechnology",
		"input": make_resources("brown",3),
		"output": [Resource("octagon"),Resource("green")],
		"upgrade": [Resource("yellow")]
		},
		{
		"name": "Genetic Engineering",
		"input": make_resources("green",3),
		"output": [Resource("blue"),Resource("black"),Resource("white")],
		"upgrade": [Resource("blue")] 
		},
		{
		"name": "Ubiquitous Cultural Repository",
		"input": make_resources("yellow",2),
		"output": [Resource("point"),Resource("white")],
		"upgrade": [Resource("black")]
		},
		{
		"name": "Clinical Immortality",
		"input": make_resources("blue",2),
		"output": [Resource("point"),Resource("green")],
		"upgrade": [Resource("black")]
		},
		{
		"name": "Atomic Transmutation",
		"input": [Resource("octagon")],
		"output": [Resource("blue"),Resource("yellow"),Resource("brown")],
		"upgrade": [Resource("blue")]
		},
		{
		"name": "Cross Species Ethical Equality",
		"input": make_resources("white",4),
		"output": [Resource("point"),Resource("point",donation=True),Resource("white",donation=True)],
		"upgrade": [Resource("octagon")]
		},
		{
		"name": "Galactic Telecomm Control",
		"input": make_resources("black", 4),
		"output": make_resources("point",3).extend(make_resources("white",2).extend([Resource("green")])),
		"upgrade": [Resource("point"),Resource("yellow")]
		},
		{
		"name": "Temporal Dilation",
		"input": make_resources("blue",4),
		"output": make_resources("point",2).extend(make_resources("brown",2).extend([Resource("octagon"),Resource("green")])),
		"upgrade": [Resource("point"),Resource("octagon",donation=True)]
		},
		{
		"name": "Social Exodus",
		"input": make_resources("white",5),
		"output": make_resources("ship",2).extend(make_resources("ship",2,donation=True).extend([Resource("yellow"),Resource("point"),Resource("yellow",donation=True),Resource("point",donation=True),Resource("blue",donation=True)])),
		"upgrade": [Resource("point"),Resource("green",donation=True)]
		},
		{
		"name": "Xeno Cultural Exchange",
		"input": make_resources("brown",5),
		"output": make_resources("white",2).extend(make_resources("green",2).extend([Resource("point"),Resource("black"),Resource("point",donation=True)])),
		"upgrade": [Resource("point"),Resource("blue",donation=True),Resource("white",donation=True)] 
		},
		{
		"name": "Megastructures",
		"input": make_resources("octagon",3),
		"output": make_resources("point",5).extend([Resource("white"),Resource("brown")]),
		"upgrade": [Resource("point"),Resource("black")]
		},
		{
		"name": "Matter Generation",
		"input": make_resources("yellow",4),
		"output": make_resources("point",2).extend([Resource("octagon"),Resource("blue"),Resource("green"),Resource("brown")]),
		"upgrade": [Resource("point"),Resource("brown")]
		},
		{
		"name": "Antimatter Power",
		"input": make_resources("brown",4),
		"output": make_resources("yellow",2).extend([Resource("blue"),Resource("green")]),
		"upgrade": [Resource("green"),Resource("white")]
		},
		{
		"name": "Achronal Analysis",
		"input": make_resources("black",3),
		"output": [Resource("octagon"),Resource("blue"),Resource("brown"),Resource("white")],
		"upgrade": [Resource("white"),Resource("yellow")]
		},
		{
		"name": "Singularity Control",
		"input": make_resources("octagon",2),
		"output": make_resources("black",2).extend([Resource("blue"),Resource("white"),Resource("green"),Resource("brown")]),
		"upgrade": [Resource("green"),Resource("green")]
		},
		{
		"name": "Interspecies Medical Exchange",
		"input": make_resources("green",4),
		"output": make_resources("green",2,donation=True).extend([Resource("point",Resource("brown"))]) ,
		"upgrade": [Resource("white"),Resource("blue")]
		},
		{
		"name": "Organic Construction",
		"input": make_resources("blue",3),
		"output": make_resources("ship",2).extend(make_resources("brown",2).extend([Resource("green"),Resource("white")])) ,
		"upgrade": [Resource("yellow")]
		},
		{
		"name": "Poly Species Corporations",
		"input": make_resources("green",5),
		"output": make_resources("ship",2).extend(make_resources("brown",2,donation=True).extend([Resource("point"),Resource("yellow"),Resource("black"),Resource("green",donation=True),Resource("white",donation=True)])) ,
		"upgrade": 
		},
		{
		"name": "Hyperspace Mining",
		"input": make_resources("yellow", 3),
		"output": [Resource("octagon"),Resource("black"),Resource("yellow",donation=True),Resource("black",donation=True)],
		"upgrade": make_resources("brown",2).extend([Resource("black")])
		},
		{
		"name": "Relic Repurposing",
		"input": make_resources("brown",2),
		"output": make_resources("ship",2).extend([Resource("white")]),
		"upgrade": [Resource("white"),Resource("green")]
		"starting": True
		},
		{
		"name": "Archaic Automated Support Network",
		"input": [],
		"output": [Resource("ship"),Resource("white"),Resource("green"),Resource("brown")],
		"upgrade": [Resource("yellow",donation=True),Resource("black",donation=True)]
		"starting": True
		},
		{
		"name": "Non-Indigenous Fauna",
		"input": make_resources("green",3),
		"output": [Resource("blue"),Resource("yellow"),Resource("brown")],
		"upgrade": [Resource("blue")]
		"starting": True
		},
		{
		"name": "Ritual Government",
		"input": make_resources("white",4),
		"output": [Resource("octagon"),Resource("black"),Resource("green")],
		"upgrade": [Resource("point")]
		"starting": True
		}
	]