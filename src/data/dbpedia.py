from SPARQLWrapper import JSON, SPARQLWrapper

from . import DataSource


class DBpediaDataSource(DataSource):
    def __init__(self, endpoint="http://dbpedia.org/sparql"):
        self.sparql = SPARQLWrapper(endpoint)

    def get_data(self):
        self.sparql.setReturnFormat(JSON)
        self.sparql.setQuery(
            """
        SELECT ?person ?name ?birthPlace ?lat ?long ?abstract ?thumbnail
        WHERE {
            ?person dbo:abstract ?abstract .
            ?person dbo:almaMater dbr:Taras_Shevchenko_National_University_of_Kyiv .
            ?person dbo:birthPlace ?birthPlace .
            ?person dbp:name ?name .
            ?person dbo:thumbnail ?thumbnail .
            ?birthPlace geo:lat ?lat .
            ?birthPlace geo:long ?long .
            FILTER (lang(?abstract) = "en")
            FILTER (lang(?name) = "en")
        }
        """
        )

        return [
            {
                "abstract": result["abstract"]["value"],
                "birthPlace": result["birthPlace"]["value"],
                "latitude": float(result["lat"]["value"]),
                "longitude": float(result["long"]["value"]),
                "name": result["name"]["value"],
                "thumbnail": result["thumbnail"]["value"],
            }
            for result in self.sparql.query().convert()["results"]["bindings"]
        ]
