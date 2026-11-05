"""Page content kept in one place so templates stay clean."""

SERVICES = [
    {
        'slug': 'new_plant',
        'icon': 'factory',
        'title': 'New Flour Mill Project Setup',
        'desc': 'End-to-end consultancy for new roller flour mills: feasibility, plant layout, building '
                'requirements, machinery selection and vendor coordination.',
        'points': ['Capacity & product-mix planning', 'Site, building & silo layout', 'Machinery selection & quotation review', 'Project timeline & vendor coordination'],
    },
    {
        'slug': 'flow_design',
        'icon': 'flow',
        'title': 'Mill Flow Sheet & Design',
        'desc': 'Practical flow diagrams for cleaning, conditioning, break, purification and reduction '
                'sections, designed for higher extraction and consistent flour quality.',
        'points': ['Cleaning & conditioning flow', 'Break, purification & reduction passages', 'Sifter & roll surface allocation', 'Flow changes for new products'],
    },
    {
        'slug': 'commissioning',
        'icon': 'wrench',
        'title': 'Erection & Commissioning',
        'desc': 'On-site supervision of machinery erection, trial runs and commissioning for both '
                'Buhler and Indian-make plants, including PLC-controlled systems.',
        'points': ['Erection supervision & alignment checks', 'No-load and load trial runs', 'Roll setting & mill balancing', 'Handover to the production team'],
    },
    {
        'slug': 'performance',
        'icon': 'trend',
        'title': 'Mill Performance Improvement',
        'desc': 'Mill audits that find losses in extraction, power and capacity, then fix roll settings, '
                'sifting, conditioning and maintenance routines.',
        'points': ['Extraction & yield audit', 'Power-per-tonne review', 'Roll, sifter & purifier optimisation', 'Preventive maintenance schedule'],
    },
    {
        'slug': 'chakki_sattu',
        'icon': 'wheat',
        'title': 'Chakki Atta & Sattu Plants',
        'desc': 'Planning and running chakki atta plants, sattu plants and allied units alongside your '
                'roller flour mill.',
        'points': ['Chakki plant layout & sizing', 'Sattu roasting & grinding lines', 'Product quality & consistency', 'Integration with the main mill'],
    },
    {
        'slug': 'training',
        'icon': 'users',
        'title': 'Quality Control & Staff Training',
        'desc': 'Wheat and flour quality practices, lab routines, and hands-on training for millers, '
                'shift in-charges and maintenance staff.',
        'points': ['Wheat intake & grading norms', 'Basic flour testing routines', 'Miller & shift in-charge training', 'Hygiene & food safety practice'],
    },
]

STATS = [
    {'num': 24, 'suffix': '+', 'label': 'Years in flour milling'},
    {'num': 4, 'suffix': '', 'label': 'Major flour mills run'},
    {'num': 400, 'suffix': '', 'label': 'TPD largest plant handled'},
    {'num': 1, 'suffix': 'st', 'label': 'Prize, plant training (CFTRI)'},
]

EXPERTISE = [
    'Roller Flour Mills', 'Buhler Plants', 'Indian-make Plants', 'PLC Automation', 'Chakki Atta Plants',
    'Sattu Plants', 'Wheat Cleaning', 'Conditioning', 'Roll Management', 'Plansifters & Purifiers',
    'Extraction Improvement', 'Staff Training',
]

CONSULT_PROCESS = [
    {'icon': 'chat', 'title': 'Discuss', 'desc': 'We understand your goals, market, budget and site, or the problem in your running mill.'},
    {'icon': 'flow', 'title': 'Plan & design', 'desc': 'Capacity, product mix, flow sheet, layout and machinery list, all on paper before money is spent.'},
    {'icon': 'wrench', 'title': 'Execute', 'desc': 'Erection supervision, trial runs and commissioning with your team on site.'},
    {'icon': 'trend', 'title': 'Optimise', 'desc': 'Fine-tune roll settings and flow, train staff, and track extraction and power cost.'},
]

FAQS = [
    {'q': 'What capacity flour mill should I start with?',
     'a': 'It depends on your local demand for maida, atta and suji, how easily you can buy wheat, your budget and the land available. We study these first and then recommend a capacity and product mix that suits you.'},
    {'q': 'Should I choose Buhler or Indian-make machinery?',
     'a': 'Both can work very well. Imported lines like Buhler usually offer more automation and consistency at a higher cost. Indian-make plants cost less and spares are easier to find. Our founder has run both as Chief Miller and can help you weigh the trade-offs.'},
    {'q': 'Can you improve the extraction of my existing mill?',
     'a': 'Usually, yes. A mill audit checks wheat conditioning, roll condition and settings, sifting and purification, and maintenance. Small corrections often give better extraction and lower power per tonne.'},
    {'q': 'Do you help with chakki atta and sattu plants?',
     'a': 'Yes. Our founder has run a 150 TPD chakki plant and a 125 TPD sattu plant alongside a roller flour mill, and we help plan and run such units.'},
    {'q': 'How long does it take to set up a roller flour mill?',
     'a': 'It depends on capacity, civil work, machinery delivery and approvals, so it can range from several months to over a year. Planning the project well at the start is the best way to avoid delays.'},
    {'q': 'Where are you based? Do you visit sites?',
     'a': 'We are based in Varanasi, Uttar Pradesh, and have worked in mills across Assam, West Bengal and Odisha. Contact us to discuss a visit to your site.'},
]

EXPERIENCE = [
    {
        'company': 'Eastern Foods Pvt. Ltd.',
        'location': 'Cuttack, Odisha',
        'position': 'Chief Miller',
        'duration': 'Nov 2016 – Present',
        'capacity': '200 TPD flour mill (Buhler) + 200 TPD flour mill (Indian)',
        'current': True,
    },
    {
        'company': 'Ganesh Grain Ltd. – Unit Padmavati Flour Mills',
        'location': 'Kolkata, West Bengal',
        'position': 'Chief Miller',
        'duration': '7 years',
        'capacity': '150 TPD flour mill (Buhler, PLC system), 150 TPD chakki plant & 125 TPD sattu plant',
    },
    {
        'company': 'Himalayan Roller Flour Mill',
        'location': 'Sevak Road, Siliguri, West Bengal',
        'position': 'Miller',
        'duration': '5 years',
        'capacity': '150 TPD flour mill (Indian plant) + 150 TPD chakki plant',
    },
    {
        'company': 'U.F. Flour Mill (Buhler)',
        'location': 'Assam',
        'position': 'Assistant Miller',
        'duration': '2 years',
        'capacity': '150 TPD flour mill',
    },
]

TRAINING_TRIPS = [
    'Karnataka State Agro Ltd., Bangalore',
    'Buhler India Ltd., Bangalore',
    'Modern Food Industries Ltd., Bangalore',
    'Quality Biscuits Pvt. Ltd., Bangalore',
    'Mill machinery manufacturers',
]

# ---------------------------------------------------------------- Flour mills in India
INDIA_FACTS = [
    {'value': '2nd', 'label': "Largest wheat producer in the world, after China"},
    {'value': '110+ MT', 'label': 'Wheat harvested a year in recent seasons (approx.)'},
    {'value': '1,000+', 'label': 'Roller flour mills in the organised sector (approx.)'},
    {'value': '~25–30%', 'label': 'Share of wheat milled by roller mills; the rest goes to chakkis'},
]

MILLING_STEPS = [
    {'title': 'Wheat intake & storage', 'desc': 'Wheat is weighed, sampled for moisture and quality, and stored in silos or godowns by grade.'},
    {'title': 'Cleaning', 'desc': 'Separators, destoners, magnets, indent cylinders and scourers remove dust, stones, iron, other seeds and broken grains.'},
    {'title': 'Conditioning (tempering)', 'desc': 'Water is added in a dampener and the wheat rests in bins for several hours so the bran toughens and the endosperm mellows.'},
    {'title': 'Break system', 'desc': 'Fluted rollermills open the grain step by step and scrape the endosperm away from the bran.'},
    {'title': 'Purification', 'desc': 'Purifiers use air and sieves to separate clean semolina from bran particles.'},
    {'title': 'Reduction', 'desc': 'Smooth rolls grind semolina and middlings into fine flour across several passages.'},
    {'title': 'Sifting', 'desc': 'Plansifters grade every stream into maida, suji/rava, atta and bran.'},
    {'title': 'Blending, enrichment & packing', 'desc': 'Flour streams are blended, optionally fortified, and packed into bags or consumer packs.'},
]

PRODUCTS = [
    {'name': 'Maida', 'desc': 'Refined white flour from the endosperm. Used by bakeries, biscuit makers and for noodles and pasta.'},
    {'name': 'Atta (whole wheat flour)', 'desc': "India's everyday flour for roti and chapati. Made in roller mills or chakki plants."},
    {'name': 'Chakki fresh atta', 'desc': 'Stone-ground atta with a coarser texture. Packaged chakki atta is a fast-growing segment.'},
    {'name': 'Suji / Rava (semolina)', 'desc': 'Granular endosperm used for upma, halwa, idli and similar foods.'},
    {'name': 'Bran (chokar)', 'desc': 'The outer layer of the grain, sold mainly as cattle feed and for high-fibre products.'},
    {'name': 'Sattu & allied products', 'desc': 'Roasted gram and other grain flours, popular in Bihar, UP and eastern India.'},
]

PLANT_TYPES = [
    {'title': 'Roller Flour Mill', 'desc': 'Large automated plants (often 100+ TPD) that make maida, suji, atta and bran using rollermills, purifiers and plansifters. Buhler and Indian manufacturers both supply complete lines.'},
    {'title': 'Chakki Atta Plant', 'desc': 'Banks of stone or emery chakkis with cleaning and sifting, built to produce traditional whole-wheat atta at industrial scale.'},
    {'title': 'Mini / Compact Flour Mill', 'desc': 'Smaller plants for regional brands and new entrepreneurs, needing less investment and space.'},
    {'title': 'Allied Plants', 'desc': 'Sattu, besan and multigrain units, often added to an existing mill to use the same infrastructure and distribution.'},
]

WHEAT_STATES = ['Uttar Pradesh', 'Madhya Pradesh', 'Punjab', 'Haryana', 'Rajasthan', 'Bihar', 'Gujarat']

MACHINERY = [
    'Pre-cleaners & separators', 'Destoners', 'Scourers', 'Indent / trieur cylinders', 'Magnetic separators',
    'Intensive dampeners', 'Rollermills (fluted & smooth)', 'Plansifters', 'Purifiers', 'Bran finishers',
    'Pneumatic & mechanical conveying', 'Flour blending & packing machines',
]

COMPLIANCE = [
    {'title': 'FSSAI licence', 'desc': 'A licence from the Food Safety and Standards Authority of India is required to make and sell flour products.'},
    {'title': 'Product standards', 'desc': 'FSSAI sets limits for atta, maida and suji, such as moisture, ash and gluten.'},
    {'title': 'Fortification (+F)', 'desc': 'Mills can fortify flour with iron, folic acid and vitamin B12 under FSSAI norms and use the +F logo.'},
    {'title': 'Legal Metrology & pollution consent', 'desc': 'Packaged goods must follow labelling rules. Mills also need state pollution control board consent, mainly for dust.'},
]

TRENDS = [
    {'title': 'Branded packaged atta', 'desc': 'Households are moving from loose flour to branded packs, which helps roller and chakki plants with strong quality control.'},
    {'title': 'Automation & PLC', 'desc': 'PLC-controlled plants cut labour, keep extraction steady and reduce downtime.'},
    {'title': 'Bakery & food processing demand', 'desc': 'Biscuits, bread, noodles and quick-service restaurants keep demand for maida and specialty flours growing.'},
    {'title': 'Energy & efficiency', 'desc': 'Power is one of the biggest running costs, so roll management and flow optimisation pay back quickly.'},
]

FLOW_STRIP = [
    {'icon': 'wheat', 'label': 'Wheat intake'},
    {'icon': 'shield', 'label': 'Cleaning'},
    {'icon': 'clock', 'label': 'Conditioning'},
    {'icon': 'wrench', 'label': 'Rollermills'},
    {'icon': 'flow', 'label': 'Sifting'},
    {'icon': 'package', 'label': 'Packing'},
]

GRAIN_PARTS = [
    {'num': 1, 'name': 'Bran', 'share': '~14–15%', 'desc': 'Protective outer layers, rich in fibre. Separated in the break system and sold as chokar (cattle feed).'},
    {'num': 2, 'name': 'Endosperm', 'share': '~82–83%', 'desc': 'The starchy, protein-rich heart of the grain. This is what becomes maida, suji and white flour.'},
    {'num': 3, 'name': 'Germ', 'share': '~2.5–3%', 'desc': 'The embryo of the seed, rich in oil and vitamins. Usually removed to improve the shelf life of flour.'},
]

# Default output split for the yield calculator (typical Indian roller mill, % of wheat milled).
CALC_DEFAULTS = [
    {'key': 'maida', 'label': 'Maida', 'pct': 58},
    {'key': 'suji', 'label': 'Suji / Rava', 'pct': 8},
    {'key': 'atta', 'label': 'Atta (resultant)', 'pct': 10},
    {'key': 'bran', 'label': 'Bran (chokar)', 'pct': 23},
    {'key': 'loss', 'label': 'Invisible loss', 'pct': 1},
]
