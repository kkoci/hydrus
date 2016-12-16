astronomy = {
	"@context": {
		"@base": "http://ontology.projectchronos.eu/astronomy",
		"schema": "https://schema.org/",
		"skos": "http://www.w3.org/2004/02/skos/core#",
		"owl": "http://www.w3.org/2002/07/owl#",
		"rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
		"dbpedia": "http://live.dbpedia.org/ontology/",
		"rdfs": "http://www.w3.org/2000/01/rdf-schema#",
		"astronomy": "http://ontology.projectchronos.eu/astronomy/",
		"defines": {
			"@reverse": "http://www.w3.org/2000/01/rdf-schema#isDefinedBy"
		},
		"chronos": "http://ontology.projectchronos.eu/chronos/"
	},
	"rdf:label": "Generic astronomical concepts ",
	"rdf:comment": "a set of concepts to be used to describe astronomical objects. Notes: 1. two different properties are applied for bodies orbiting a star (property \"orbiting\") and orbiting a planet (property \"orbitsPlanet\") - 2. PlanetaryBody entity is a wider group for any object subject permanently to the gravity of a Planet. Planet entity is for the planet itself",
	"@type": "http://www.w3.org/2002/07/owl#Ontology",
	"defines": [{
		"owl:sameAs": {
			"@id": "http://umbel.org/umbel/rc/AstronomicalObject.n3"
		},
		"rdf:label": "AstronomicalObject",
		"rdf:comment": "an astronomical body (from a natural satellite size up) or a group of astronomical body",
		"@id": "http://ontology.projectchronos.eu/astronomy/AstronomicalObject",
		"@type": "http://www.w3.org/2002/07/owl#Class"
	}, {
		"rdf:label": "Planetary_system",
		"rdf:comment": "Solar System is a planetary system - see solarsystem vocabulary",
		"@type": "http://www.w3.org/2002/07/owl#Class",
		"owl:sameAs": {
			"@id": "http://live.dbpedia.org/data/Planetary_system.ntriples"
		},
		"rdfs:subClassOf": {
			"@id": "http://ontology.projectchronos.eu/astronomy/AstronomicalObject"
		},
		"@id": "http://ontology.projectchronos.eu/astronomy/Planetary_system"
	}, {
		"rdf:label": "Star",
		"rdf:comment": "a star",
		"@type": "http://www.w3.org/2002/07/owl#Class",
		"owl:sameAs": [{
			"@id": "http://umbel.org/umbel/rc/Star.n3"
		}, {
			"@id": "http://sw.opencyc.org/concept/Mx4rvVi80ZwpEbGdrcN5Y29ycA"
		}, {
			"@id": "http://live.dbpedia.org/data/Star.n3"
		}],
		"rdfs:subClassOf": {
			"@id": "http://ontology.projectchronos.eu/astronomy/AstronomicalObject"
		},
		"@id": "http://ontology.projectchronos.eu/astronomy/Star"
	}, {
		"skos:altLabel": "a general astronomical object with the characteristics of a planet or any natural object under gravitational influence of a planet",
		"rdf:label": "PlanetaryBody",
		"rdf:comment": "a document representing a general planet-shaped body or natural satellite or dust or rock or macroscopic particle of matter",
		"@id": "http://ontology.projectchronos.eu/astronomy/PlanetaryBody",
		"@type": "http://www.w3.org/2002/07/owl#Class"
	}, {
		"skos:altLabel": "a general astronomical object with the characteristics of a planet",
		"rdf:label": "Planet",
		"rdf:comment": "a document representing a general planet-shaped astronomical body",
		"@type": "http://www.w3.org/2002/07/owl#Class",
		"owl:sameAs": [{
			"@id": "http://sw.opencyc.org/concept/Mx4rvVjRL5wpEbGdrcN5Y29ycA"
		}, {
			"@id": "http://live.dbpedia.org/data/Planet.n3"
		}],
		"rdfs:subClassOf": {
			"@id": "http://ontology.projectchronos.eu/astronomy/PlanetaryBody"
		},
		"@id": "http://ontology.projectchronos.eu/astronomy/Planet"
	}, {
		"rdf:label": "orbiting",
		"rdf:comment": "this property describe the generic astronomical object-object gravitational interaction",
		"@type": "http://www.w3.org/2002/07/owl#ObjectProperty",
		"owl:sameAs": {
			"@id": "http://sw.opencyc.org/concept/Mx4rvmlCvZwpEbGdrcN5Y29ycA"
		},
		"rdf:domain": {
			"@id": "http://ontology.projectchronos.eu/astronomy/AstronomicalObject"
		},
		"rdf:range": {
			"@id": "http://ontology.projectchronos.eu/astronomy/Star"
		},
		"@id": "http://ontology.projectchronos.eu/astronomy/orbiting"
	}, {
		"rdf:label": "orbitsPlanet",
		"rdf:domain": [{
			"@id": "http://ontology.projectchronos.eu/astronomy/Natural_satellite"
		}, {
			"@id": "http://ontology.projectchronos.eu/astronomy/PlanetaryBody"
		}],
		"@type": "http://www.w3.org/2002/07/owl#ObjectProperty",
		"rdf:comment": "this property describe the Moon-Planet gravitational interaction",
		"rdf:range": [{
			"@id": "http://ontology.projectchronos.eu/astronomy/PlanetaryBody"
		}, {
			"@id": " http://ontology.projectchronos.eu/astronomy/DwarfPlanet"
		}],
		"rdfs:subClassOf": {
			"@id": ""
		},
		"@id": "http://ontology.projectchronos.eu/astronomy/orbitsPlanet"
	}, {
		"rdfs:sameAs": [{
			"@id": "http://umbel.org/umbel/rc/SubplanetaryStellarOrbiter.n3"
		}, {
			"@id": "http://live.dbpedia.org/data/Asteroid.ntriples"
		}],
		"rdf:label": "Asteroid",
		"rdf:comment": "a document representing an asteroid",
		"@type": "http://www.w3.org/2002/07/owl#Class",
		"owl:sameAs": {
			"@id": "http://live.dbpedia.org/data/Asteroid.ntriples"
		},
		"@id": "http://ontology.projectchronos.eu/astronomy/Asteroid"
	}, {
		"rdfs:sameAs": [{
			"@id": "http://umbel.org/umbel/rc/SubplanetaryStellarOrbiter.n3"
		}, {
			"@id": "http://live.dbpedia.org/data/Meteoroid.ntriples"
		}],
		"rdf:label": "Meteoroid",
		"rdf:comment": "a document representing a meteoroid",
		"@type": "http://www.w3.org/2002/07/owl#Class",
		"owl:sameAs": {
			"@id": "http://umbel.org/umbel/rc/Meteoroid.n3"
		},
		"@id": "http://ontology.projectchronos.eu/astronomy/Meteoroid"
	}, {
		"rdfs:sameAs": [{
			"@id": "http://umbel.org/umbel/rc/SubplanetaryStellarOrbiter.n3"
		}, {
			"@id": "http://live.dbpedia.org/data/Comet.ntriples"
		}],
		"rdf:label": "Comet",
		"rdf:comment": "a document representing a comet",
		"@type": "http://www.w3.org/2002/07/owl#Class",
		"owl:sameAs": {
			"@id": "http://umbel.org/umbel/rc/Comet.n3"
		},
		"@id": "http://ontology.projectchronos.eu/astronomy/Comet"
	}, {
		"owl:sameAs": [{
			"@id": "http://umbel.org/umbel/rc/MoonOfAPlanet.n3"
		}, {
			"@id": "http://live.dbpedia.org/data/Natural_satellite.ntriples"
		}, {
			"@id": "http://sw.opencyc.org/concept/Mx4rvfn7-pwpEbGdrcN5Y29ycA"
		}],
		"rdf:label": "Natural_satellite",
		"rdf:comment": "a document representing a natural satellite or moon",
		"@id": "http://ontology.projectchronos.eu/astronomy/Natural_satellite",
		"@type": "http://www.w3.org/2002/07/owl#Class"
	}, {
		"rdf:label": "TerrestrialPlanet",
		"rdf:comment": "a document representing a solid/rocky planet",
		"@type": "http://www.w3.org/2002/07/owl#Class",
		"owl:sameAs": {
			"@id": "http://umbel.org/umbel/rc/TerrestrialPlanet.n3"
		},
		"rdfs:subClassOf": {
			"@id": "http://ontology.projectchronos.eu/astronomy/PlanetaryBody"
		},
		"@id": "http://ontology.projectchronos.eu/astronomy/TerrestrialPlanet"
	}, {
		"rdf:label": "SolidPlanetaryBody",
		"rdf:comment": "planet composed primarily of solid substances",
		"@type": "http://www.w3.org/2002/07/owl#Class",
		"owl:sameAs": {
			"@id": "http://umbel.org/umbel/rc/SolidPlanetaryBody.n3"
		},
		"rdfs:subClassOf": {
			"@id": "http://ontology.projectchronos.eu/astronomy/PlanetaryBody"
		},
		"@id": "http://ontology.projectchronos.eu/astronomy/SolidPlanetaryBody"
	}, {
		"rdf:label": "IcyPlanetaryBody",
		"rdf:comment": "a document representing an icy body",
		"@type": "http://www.w3.org/2002/07/owl#Class",
		"owl:sameAs": {
			"@id": "http://umbel.org/umbel/rc/IcyPlanetaryBody.n3"
		},
		"rdfs:subClassOf": {
			"@id": "http://ontology.projectchronos.eu/astronomy/PlanetaryBody"
		},
		"@id": "http://ontology.projectchronos.eu/astronomy/IcyPlanetaryBody"
	}, {
		"rdf:label": "Ice_giant",
		"rdf:comment": "a gas giant with less helium/hydrogen and more 'ices', Uranus and Neputne subclass",
		"@type": "http://www.w3.org/2002/07/owl#Class",
		"owl:sameAs": {
			"@id": "http://live.dbpedia.org/data/Ice_giant.ntriples"
		},
		"rdfs:subClassOf": {
			"@id": "http://ontology.projectchronos.eu/astronomy/GasGiant"
		},
		"@id": "http://ontology.projectchronos.eu/astronomy/Ice_giant"
	}, {
		"rdf:label": "GasGiant",
		"rdf:comment": "a Jovian planet, a document representing a Jovian planet",
		"@id": "http://ontology.projectchronos.eu/astronomy/GasGiant",
		"@type": "http://www.w3.org/2002/07/owl#Class",
		"rdfs:subClassOf": {
			"@id": "http://ontology.projectchronos.eu/astronomy/PlanetaryBody"
		},
		"@owl:sameAs": {
			"@id": "http://umbel.org/umbel/rc/GasGiant.n3"
		}
	}, {
		"rdf:label": "DwarfPlanet",
		"rdf:comment": "a trans-neptunian object with planet-like size",
		"@id": "http://ontology.projectchronos.eu/astronomy/DwarfPlanet",
		"@type": "http://www.w3.org/2002/07/owl#Class",
		"astronomy:orbiting": {
			"@id": "http://ontology.projectchronos.eu/astronomy/Sun"
		},
		"rdfs:subClassOf": {
			"@id": "http://umbel.org/umbel/rc/SubplanetaryStellarOrbiter.n3"
		},
		"@owl:sameAs": {
			"@id": " http://live.dbpedia.org/data/Dwarf_planet.ntriples"
		}
	}, {
		"rdf:label": "RockyPlanetaryBody",
		"rdf:comment": "a document representing a rocky body",
		"@type": "http://www.w3.org/2002/07/owl#Class",
		"owl:sameAs": {
			"@id": "http://umbel.org/umbel/rc/RockyPlanetaryBody.n3"
		},
		"rdfs:subClassOf": {
			"@id": "http://ontology.projectchronos.eu/astronomy/PlanetaryBody"
		},
		"@id": "http://ontology.projectchronos.eu/astronomy/RockyPlanetaryBody"
	}, {
		"owl:sameAs": {
			"@id": "http://umbel.org/umbel/rc/SubplanetaryStellarOrbiter.n3"
		},
		"rdf:label": "SubplanetaryStellarOrbiter",
		"rdf:comment": "a smaller body orbiting around stars or planets, a document representing smaller body orbiting around stars or planets",
		"@id": "http://ontology.projectchronos.eu/astronomy/SubplanetaryStellarOrbiter",
		"@type": "http://www.w3.org/2002/07/owl#Class"
	}, {
		"rdf:label": "FluidPlanetaryBody",
		"rdf:comment": "a document representing a non-solid planet",
		"@type": "http://www.w3.org/2002/07/owl#Class",
		"owl:sameAs": {
			"@id": "http://umbel.org/umbel/rc/FluidPlanetaryBody.n3"
		},
		"rdfs:subClassOf": {
			"@id": "http://ontology.projectchronos.eu/astronomy/PlanetaryBody"
		},
		"@id": "http://ontology.projectchronos.eu/astronomy/FluidPlanetaryBody"
	}, {
		"owl:sameAs": {
			"@id": "http://umbel.org/umbel/rc/AstronomicalObservatory.n3"
		},
		"rdf:label": "AstronomicalObservatory",
		"rdf:comment": "a document representing an astronomical observatory",
		"@id": "http://ontology.projectchronos.eu/astronomy/AstronomicalObservatory",
		"@type": "http://www.w3.org/2002/07/owl#Class"
	}, {
		"owl:sameAs": {
			"@id": "http://live.dbpedia.org/ontology/CelestialBody.ntriples"
		},
		"rdf:label": "CelestialBody",
		"rdf:comment": "a document representing a generic celestial body",
		"@id": "http://ontology.projectchronos.eu/astronomy/CelestialBody",
		"@type": "http://www.w3.org/2002/07/owl#Class"
	}, {
		"owl:sameAs": {
			"@id": "http://live.dbpedia.org/ontology/Outer_space.ntriples"
		},
		"rdf:label": "Outer_space",
		"rdf:comment": "a document representing the open space outside atmosphere, from Low Earth Orbit to Extra Galactic Space",
		"@id": "http://ontology.projectchronos.eu/astronomy/Outer_space",
		"@type": "http://www.w3.org/2002/07/owl#Class"
	}, {
		"rdf:label": "PlanetaryScience",
		"owl:sameAs": {
			"@id": "http://live.dbpedia.org/data/Planetary_science.ntriples"
		},
		"rdfs:subClassOf": {
			"@id": "http://ontology.projectchronos.eu/sensors/FieldOfResearch"
		},
		"@id": "http://ontology.projectchronos.eu/astronomy/PlanetaryScience",
		"@type": "http://www.w3.org/2002/07/owl#Class"
	}, {
		"rdf:label": "AtmosphericScience",
		"owl:sameAs": {
			"@id": "http://umbel.org/umbel/rc/AtmosphericScience.n3"
		},
		"rdfs:subClassOf": {
			"@id": "http://ontology.projectchronos.eu/sensors/PlanetaryScience"
		},
		"@id": "http://ontology.projectchronos.eu/astronomy/AtmosphericScience",
		"@type": "http://www.w3.org/2002/07/owl#Class"
	}, {
		"rdf:label": "Cosmology",
		"owl:sameAs": [{
			"@id": "http://umbel.org/umbel/rc/Cosmology.n3"
		}, {
			"@id": "http://live.dbpedia.org/data/Cosmology.ntriples"
		}],
		"rdfs:subClassOf": {
			"@id": "http://ontology.projectchronos.eu/sensors/FieldOfResearch"
		},
		"@id": "http://ontology.projectchronos.eu/astronomy/Cosmology",
		"@type": "http://www.w3.org/2002/07/owl#Class"
	}, {
		"rdf:label": "ExtragalacticAstronomy",
		"owl:sameAs": {
			"@id": "http://live.dbpedia.org/data/Extragalactic_astronomy.ntriples"
		},
		"rdfs:subClassOf": {
			"@id": "http://ontology.projectchronos.eu/sensors/FieldOfResearch"
		},
		"@id": "http://ontology.projectchronos.eu/astronomy/ExtragalacticAstronomy",
		"@type": "http://www.w3.org/2002/07/owl#Class"
	}, {
		"rdf:label": "GalacticAstronomy",
		"owl:sameAs": {
			"@id": "http://live.dbpedia.org/data/Galactic_astronomy.ntriples"
		},
		"rdfs:subClassOf": {
			"@id": "http://ontology.projectchronos.eu/sensors/FieldOfResearch"
		},
		"@id": "http://ontology.projectchronos.eu/astronomy/GalacticAstronomy",
		"@type": "http://www.w3.org/2002/07/owl#Class"
	}, {
		"rdf:label": "PlanetaryAstronomy",
		"rdfs:subClassOf": {
			"@id": "http://ontology.projectchronos.eu/sensors/PlanetaryScience"
		},
		"@id": "http://ontology.projectchronos.eu/sensors/PlanetaryAstronomy",
		"@type": "http://www.w3.org/2002/07/owl#Class"
	}, {
		"rdf:label": "PlanetaryGeology",
		"rdfs:subClassOf": {
			"@id": "http://ontology.projectchronos.eu/sensors/PlanetaryScience"
		},
		"@id": "http://ontology.projectchronos.eu/sensors/PlanetaryGeology",
		"@type": "http://www.w3.org/2002/07/owl#Class"
	}, {
		"rdf:label": "SolarAstronomy",
		"rdfs:subClassOf": {
			"@id": "http://ontology.projectchronos.eu/sensors/FieldOfResearch"
		},
		"@id": "http://ontology.projectchronos.eu/sensors/SolarAstronomy",
		"@type": "http://www.w3.org/2002/07/owl#Class"
	}, {
		"rdf:label": "StellarAstronomy",
		"rdfs:subClassOf": {
			"@id": "http://ontology.projectchronos.eu/sensors/FieldOfResearch"
		},
		"@id": "http://ontology.projectchronos.eu/sensors/StellarAstronomy",
		"@type": "http://www.w3.org/2002/07/owl#Class"
	}],
	"@id": ""
}