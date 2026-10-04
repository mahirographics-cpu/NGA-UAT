"""
exam_data.py
-------------
UAT Mock Exam question bank for the Next Grade Academy Telegram bot.

Schema matches exam.py / results.py / review.py exactly:
    questions = [ {section, question, options[4], answer, explanation}, ... ]

- section   : "Verbal" or "Quantitative" (these are the two buckets
              results.py scores and nextgread.py advertises)
- options   : plain list of 4 strings, shown in order as A/B/C/D
- answer    : the correct letter ("A"/"B"/"C"/"D")
- explanation: shown in review.py under "Review Mistakes" for any
               question left unanswered or answered incorrectly
"""

questions = [
    # ============== VERBAL: Sentence Completion ==============
    {
        "section": "Verbal",
        "question": "Although the experiment failed initially, the researchers remained ________ and continued improving their methods.",
        "options": ["discouraged", "determined", "indifferent", "careless"],
        "answer": "B",
        "explanation": "The sentence contrasts an initial failure with continued effort ('continued improving'), so the missing word must express persistence. 'Determined' fits; the others would contradict the idea of continuing to improve.",
    },
    {
        "section": "Verbal",
        "question": "Although the proposal appeared attractive at first, a closer examination revealed several ______ flaws.",
        "options": ["trivial", "concealed", "temporary", "harmless"],
        "answer": "B",
        "explanation": "'Although...at first' signals a contrast: something not obvious initially became visible on closer look. 'Concealed' (hidden) flaws matches this; trivial/temporary/harmless don't fit 'closer examination revealed'.",
    },
    {
        "section": "Verbal",
        "question": "The manager's explanation was so ______ that everyone understood the new procedure immediately.",
        "options": ["ambiguous", "concise", "obscure", "contradictory"],
        "answer": "B",
        "explanation": "Immediate understanding by everyone implies the explanation was clear and to the point. 'Concise' fits; ambiguous, obscure, and contradictory would all make understanding harder.",
    },
    {
        "section": "Verbal",
        "question": "The professor encouraged students to question accepted ideas rather than ________ them without evidence.",
        "options": ["accepting", "rejecting", "discussing", "publishing"],
        "answer": "A",
        "explanation": "'Rather than' sets up a contrast with 'question': the opposite of questioning ideas is simply accepting them uncritically. 'Accepting' completes that contrast.",
    },
    {
        "section": "Verbal",
        "question": "Despite repeated setbacks, the scientist remained ________, convinced that perseverance would eventually lead to success.",
        "options": ["apathetic", "resolute", "skeptical", "hesitant"],
        "answer": "B",
        "explanation": "'Despite repeated setbacks' plus 'convinced perseverance would lead to success' both point to firm resolve. 'Resolute' (determined, unwavering) matches; the others contradict confident perseverance.",
    },

    # ============== VERBAL: Reading Passage ==============
    {
        "section": "Verbal",
        "question": (
            "Read the passage, then answer the question.\n\n"
            "\"Scientists once believed that memory worked like a video recorder, storing "
            "experiences exactly as they occurred. Modern research, however, suggests that "
            "memory is reconstructive. Rather than replaying events perfectly, the brain "
            "rebuilds memories each time they are recalled. As a result, details may change "
            "over time, especially when influenced by new information or personal beliefs. "
            "Although memory is generally reliable for everyday life, it is not an exact "
            "record of the past.\"\n\n"
            "According to the passage, modern researchers believe that memory"
        ),
        "options": [
            "records every detail perfectly",
            "disappears over time",
            "reconstructs past experiences rather than reproducing them exactly",
            "cannot be trusted at all",
        ],
        "answer": "C",
        "explanation": "The passage states directly that memory is 'reconstructive' and that the brain 'rebuilds memories each time they are recalled' rather than replaying them perfectly.",
    },
    {
        "section": "Verbal",
        "question": (
            "Read the passage, then answer the question.\n\n"
            "\"Scientists once believed that memory worked like a video recorder, storing "
            "experiences exactly as they occurred. Modern research, however, suggests that "
            "memory is reconstructive. Rather than replaying events perfectly, the brain "
            "rebuilds memories each time they are recalled. As a result, details may change "
            "over time, especially when influenced by new information or personal beliefs. "
            "Although memory is generally reliable for everyday life, it is not an exact "
            "record of the past.\"\n\n"
            "Which statement is supported by the passage?"
        ),
        "options": [
            "Personal beliefs may influence remembered events.",
            "Memory is completely inaccurate.",
            "Scientists no longer study memory.",
            "Human memory never changes.",
        ],
        "answer": "A",
        "explanation": "The passage says memory details 'may change over time, especially when influenced by new information or personal beliefs,' directly supporting this option. It also calls memory 'generally reliable,' ruling out the others.",
    },

    # ============== VERBAL: Logical Reasoning ==============
    {
        "section": "Verbal",
        "question": "\"If the bridge is unsafe, engineers would have closed it. The bridge has not been closed. Therefore, the bridge is safe.\" Which assumption is this argument most dependent on?",
        "options": [
            "Bridges are inspected annually",
            "Engineers always have complete and timely information about the bridge's condition",
            "The bridge was built recently",
            "Public transportation is available as an alternative",
        ],
        "answer": "B",
        "explanation": "The argument only works if engineers would actually know about and act on any unsafe condition. If they might lack complete or timely information, the bridge could be unsafe without having been closed.",
    },
    {
        "section": "Verbal",
        "question": "Every physician is a university graduate. Some university graduates are researchers. Which statement must be true?",
        "options": [
            "Every researcher is a physician.",
            "Some physicians are researchers.",
            "No researchers are physicians.",
            "None of the above.",
        ],
        "answer": "D",
        "explanation": "The premises don't guarantee any overlap (or lack of it) between physicians and researchers, so none of the other options must be true.",
    },
    {
        "section": "Verbal",
        "question": "If every Zor is a Lax, and no Lax is a Mep, then",
        "options": [
            "Some Zors are Meps.",
            "Every Mep is a Lax.",
            "No Zor is a Mep.",
            "Every Lax is a Zor.",
        ],
        "answer": "C",
        "explanation": "Since every Zor is a Lax, and no Lax is a Mep, no Zor can be a Mep either — Zors are entirely inside the Lax group, which never overlaps with Mep.",
    },
    {
        "section": "Verbal",
        "question": "If all roses are flowers and some flowers fade quickly, which statement must be true?",
        "options": [
            "All roses fade quickly.",
            "Some roses fade quickly.",
            "Roses are flowers.",
            "No flowers are roses.",
        ],
        "answer": "C",
        "explanation": "'All roses are flowers' is stated directly as a premise, so it must be true. We can't conclude anything definite about roses fading, since 'some flowers fade quickly' doesn't specify which ones.",
    },
    {
        "section": "Verbal",
        "question": "Every student who studies hard passes the exam. Tom did not pass the exam. What can you conclude?",
        "options": [
            "Tom studied hard",
            "Nothing can be concluded about Tom's studying",
            "Tom did not study hard",
            "Tom passed the exam",
        ],
        "answer": "C",
        "explanation": "This is a contrapositive: 'studies hard -> passes' means 'does not pass -> did not study hard'. Since Tom did not pass, he did not study hard.",
    },
    {
        "section": "Verbal",
        "question": "If every scholarship student studies mathematics, and Hana is a scholarship student, then which statement must be true?",
        "options": [
            "Hana studies mathematics.",
            "Hana is a mathematics teacher.",
            "Hana studies only mathematics.",
            "Everyone studying mathematics has a scholarship.",
        ],
        "answer": "A",
        "explanation": "Direct application of the rule 'every scholarship student studies mathematics' to Hana, who is a scholarship student.",
    },
    {
        "section": "Verbal",
        "question": "Some computers are laptops. All laptops are portable. Which conclusion must be true?",
        "options": [
            "All computers are portable.",
            "Some portable devices are laptops.",
            "Some computers are portable.",
            "Every portable device is a computer.",
        ],
        "answer": "C",
        "explanation": "Since some computers are laptops, and all laptops are portable, those same computers must be portable — so at least 'some computers are portable'. We can't say ALL computers are, since only some are laptops.",
    },
    {
        "section": "Verbal",
        "question": "All scholarship recipients passed the entrance examination. Some students who passed the entrance examination later withdrew from the university. Which statement must be true?",
        "options": [
            "Some students who withdrew passed the entrance examination.",
            "All students who passed received scholarships.",
            "No scholarship recipients withdrew.",
            "Every university student passed the entrance examination.",
        ],
        "answer": "A",
        "explanation": "The second premise directly states that some students who passed the entrance exam later withdrew — exactly what this option restates.",
    },

    # ============== VERBAL: Vocabulary ==============
    {
        "section": "Verbal",
        "question": "The word pragmatic most nearly means",
        "options": ["Emotional", "Practical and realistic", "Imaginative", "Arrogant"],
        "answer": "B",
        "explanation": "'Pragmatic' means dealing with things sensibly and realistically, based on practical rather than theoretical considerations.",
    },
    {
        "section": "Verbal",
        "question": "The word mitigate most nearly means",
        "options": ["strengthen", "ignore", "reduce the severity of", "increase"],
        "answer": "C",
        "explanation": "'Mitigate' means to make something less severe, serious, or painful. 'Strengthen' and 'increase' are near opposites.",
    },
    {
        "section": "Verbal",
        "question": "The word obsolete most nearly means",
        "options": ["modern", "no longer in use", "expensive", "attractive"],
        "answer": "B",
        "explanation": "'Obsolete' describes something outdated or no longer produced/used because something newer has replaced it.",
    },
    {
        "section": "Verbal",
        "question": "Choose the word closest in meaning to METICULOUS.",
        "options": ["Careless", "Ordinary", "Reckless", "Thorough"],
        "answer": "D",
        "explanation": "'Meticulous' means showing great attention to detail and being very careful and precise, closest to 'thorough'. Careless and reckless are near opposites.",
    },
    {
        "section": "Verbal",
        "question": "Which word is the opposite of SCARCE?",
        "options": ["Rare", "Insufficient", "Abundant", "Limited"],
        "answer": "C",
        "explanation": "'Scarce' means in short supply; its opposite is 'abundant' (plentiful). Rare, insufficient, and limited are all synonyms of scarce, not opposites.",
    },

    # ============== VERBAL: Analogy ==============
    {
        "section": "Verbal",
        "question": "Pen is to Writer as Scalpel is to",
        "options": ["Patient", "Hospital", "Nurse", "Surgeon"],
        "answer": "D",
        "explanation": "A pen is the primary tool used by a writer; a scalpel is the primary tool used by a surgeon. The relationship is 'tool used by this professional'.",
    },
    {
        "section": "Verbal",
        "question": "Optimist is to Hope as Pessimist is to",
        "options": ["Success", "Doubt", "Joy", "Wisdom"],
        "answer": "B",
        "explanation": "An optimist is characterized by hope; a pessimist is characterized by doubt (negative expectation).",
    },
    {
        "section": "Verbal",
        "question": "Blueprint : Building :: Score : ______",
        "options": ["Orchestra", "Composer", "Symphony", "Musician"],
        "answer": "C",
        "explanation": "A blueprint is the plan used to construct a building; a musical score is the plan used to create a symphony. 'Design document -> finished creation'.",
    },
    {
        "section": "Verbal",
        "question": "Erosion : Rock :: Corrosion : ______",
        "options": ["Steel", "Water", "Fire", "Wind"],
        "answer": "A",
        "explanation": "Erosion is the gradual wearing away of rock; corrosion is the gradual chemical wearing away of a metal such as steel.",
    },
    {
        "section": "Verbal",
        "question": "Constitution : Nation :: Genome : ______",
        "options": ["Animal", "Species", "Cell", "Organism"],
        "answer": "D",
        "explanation": "A constitution is the foundational governing information for a nation; a genome is the foundational genetic information for an organism.",
    },

    # ============== QUANTITATIVE ==============
    {
        "section": "Quantitative",
        "question": "A school library has 240 books. If 15% are science books and one-third of the science books are borrowed, how many science books remain in the library?",
        "options": ["12", "24", "30", "36"],
        "answer": "B",
        "explanation": "15% of 240 = 36 science books. One-third borrowed = 12 borrowed, leaving 36 - 12 = 24 science books.",
    },
    {
        "section": "Quantitative",
        "question": "A number is increased by 20%, then decreased by 20%. The final value is what percent of the original?",
        "options": ["94%", "96%", "98%", "100%"],
        "answer": "B",
        "explanation": "Increase by 20% multiplies by 1.20; decrease that result by 20% multiplies by 0.80. Combined: 1.20 x 0.80 = 0.96, i.e. 96% of the original.",
    },
    {
        "section": "Quantitative",
        "question": "Two numbers differ by 8 and their product is 240. The larger number is",
        "options": ["20", "24", "28", "30"],
        "answer": "A",
        "explanation": "Let the numbers be x and x-8. x(x-8) = 240 -> x^2 - 8x - 240 = 0 -> (x-20)(x+12) = 0 -> x = 20. The larger number is 20 (smaller is 12; 20x12=240, difference=8).",
    },
    {
        "section": "Quantitative",
        "question": "A committee of 3 is chosen from 6 men and 4 women. If the committee must contain exactly two women, how many different committees are possible?",
        "options": ["60", "72", "80", "90"],
        "answer": "A",
        "explanation": "Choose 2 women from 4: C(4,2)=6. Choose 1 man from 6: C(6,1)=6. Note: 6 x 6 = 36 with these exact numbers, which doesn't match any listed option — this likely has a typo in the original numbers (e.g. 5 women would give C(5,2) x C(6,1) = 10 x 6 = 60, matching 'A'). Worth double-checking against your source before publishing.",
    },
    {
        "section": "Quantitative",
        "question": "A cube has volume 343 cm^3. Its total surface area is",
        "options": ["196 cm^2", "245 cm^2", "294 cm^2", "343 cm^2"],
        "answer": "C",
        "explanation": "Volume = side^3 = 343, so side = 7 cm. Total surface area of a cube = 6 x side^2 = 6 x 49 = 294 cm^2.",
    },
    {
        "section": "Quantitative",
        "question": "The point (3,4) is reflected across the x-axis and then across the y-axis. The final coordinates are",
        "options": ["(-3,4)", "(3,-4)", "(-3,-4)", "(4,-3)"],
        "answer": "C",
        "explanation": "Reflecting (3,4) across the x-axis gives (3,-4). Reflecting that across the y-axis gives (-3,-4).",
    },
    {
        "section": "Quantitative",
        "question": "A car rental agency charges 15 Birr a day plus 0.12 Birr per mile. What is the total cost of traveling 400 miles over 3 days?",
        "options": ["45", "48", "93", "144"],
        "answer": "C",
        "explanation": "Daily charge: 15 x 3 = 45 Birr. Mileage charge: 0.12 x 400 = 48 Birr. Total: 45 + 48 = 93 Birr.",
    },
    {
        "section": "Quantitative",
        "question": "What number do you get when you multiply the distinct prime factors of 56?",
        "options": ["4", "14", "7", "28"],
        "answer": "B",
        "explanation": "56 = 2^3 x 7, so its distinct prime factors are 2 and 7. Multiplying: 2 x 7 = 14.",
    },
    {
        "section": "Quantitative",
        "question": "Set P is the set of all positive multiples of 4 less than 30. Set Q is the set of all positive multiples of 6 less than 30. How many numbers are in the intersection of sets P and Q?",
        "options": ["0", "1", "2", "3"],
        "answer": "C",
        "explanation": "P = {4,8,12,16,20,24,28}. Q = {6,12,18,24}. The intersection is {12, 24} — 2 numbers.",
    },
    {
        "section": "Quantitative",
        "question": "How many even integers are between -10 and 10?",
        "options": ["7", "8", "9", "11"],
        "answer": "C",
        "explanation": "Strictly between -10 and 10, the even integers are -8,-6,-4,-2,0,2,4,6,8 — 9 numbers.",
    },
    {
        "section": "Quantitative",
        "question": "Twelve more than twice a certain number is six fewer than three times the number. What is the number?",
        "options": ["16", "18", "6", "12"],
        "answer": "B",
        "explanation": "2x + 12 = 3x - 6 -> 18 = x. The number is 18.",
    },
    {
        "section": "Quantitative",
        "question": "The smallest 3-digit prime number is:",
        "options": ["129", "139", "149", "159"],
        "answer": "B",
        "explanation": "Among these options, 129 (=3x43) and 159 (=3x53) aren't prime. 139 is prime and smaller than 149. (The true smallest 3-digit prime overall is 101, not listed here.)",
    },
    {
        "section": "Quantitative",
        "question": "39 persons can repair a road in 12 days, working 5 hours a day. In how many days will 30 persons, working 6 hours a day, complete the work?",
        "options": ["11", "13", "14", "15"],
        "answer": "B",
        "explanation": "Total work = 39 x 12 x 5 = 2340 person-hours. For 30 persons at 6 hrs/day: 2340 / (30 x 6) = 2340 / 180 = 13 days.",
    },
    {
        "section": "Quantitative",
        "question": "If 3 to the power of (2x-1) = 81, then x equals",
        "options": ["2", "2.5", "3", "3.5"],
        "answer": "B",
        "explanation": "81 = 3^4, so 2x - 1 = 4 -> 2x = 5 -> x = 2.5.",
    },
    {
        "section": "Quantitative",
        "question": "The mean of 5 numbers is 10. A sixth number, 25, is added to the set. What is the new mean?",
        "options": ["10", "11", "12.5", "15"],
        "answer": "C",
        "explanation": "Mean of 5 numbers is 10, so their total is 5 x 10 = 50. Adding 25 gives a new total of 75, across 6 numbers now. New mean = 75 / 6 = 12.5.",
    },
]
