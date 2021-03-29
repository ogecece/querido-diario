from gazette.spiders.base.sigpub import SigpubGazetteSpider


class PbAssociacaoMunicipiosSpider(SigpubGazetteSpider):
    name = "pb_associacao_municipios"
    TERRITORY_ID = "2500000"
    CALENDAR_URL = "http://www.diariomunicipal.com.br/famup"
    TERRITORIES_COVERAGE = [
        "2503001",
        "2503100",
        "2504405",
        "2504504",
        "2507804",
        "2508505",
        "2510808",
        "2511004",
        "2513802",
        "2514909",
        "2500700",
        "2500106",
        "2500403",
        "2500601",
        "2500775",
        "2500908",
        "2501609",
        "2501708",
        "2501807",
        "2502052",
        "2502151",
        "2502409",
        "2503407",
        "2503555",
        "2503605",
        "2503753",
        "2504207",
        "2504801",
        "2505303",
        "2505600",
        "2506004",
        "2506707",
        "2507002",
        "2507309",
        "2513653",
        "2507705",
        "2507903",
        "2508554",
        "2508802",
        "2509008",
        "2509156",
        "2509206",
        "2509305",
        "2509339",
        "2509503",
        "2509602",
        "2509701",
        "2510006",
        "2510501",
        "2510600",
        "2510907",
        "2511301",
        "2511400",
        "2511806",
        "2512002",
        "2512101",
        "2512309",
        "2512606",
        "2512903",
        "2513158",
        "2513968",
        "2513984",
        "2514107",
        "2514206",
        "2514404",
        "2514651",
        "2515005",
        "2515104",
        "2515203",
        "2515302",
        "2515708",
        "2516102",
        "2516607",
        "2516904",
    ]
