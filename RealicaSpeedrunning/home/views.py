from django.shortcuts import render, redirect
from register.models import Member
import time as t

# Create your views here.

def goto_login(request):
    return redirect('/login')

def mainview(request):
    if request.user.is_authenticated:
        return render(request, 'home/home.html', {'members': Member.objects.all().values()})
    
    else:
        return redirect('/login')

def testview(request):

    def spellcheck(string, correct):
        s, c = [], []
        stats = {'p': 0}

        for i in string:
            s.append(i)

        for i in correct:
            c.append(i)

        for i in range(len(correct)):
            try:
                if s[i] == c[i]:
                    stats['p'] += 1
            except:
                continue
        score = round(stats.get("p") / len(correct) * 100)
        return score
    
    if request.user.is_authenticated:
        tests = {
            '1881-1890': '1872. aastal asutati fond Tallinna Peetri Reaalkooli rajamiseks Peeter I 200. sünniaastapäevaks. 1881. aasta sügisel alustaski saksakeelne poeglaste keskkool tööd. Esimeseks direktoriks sai matemaatikaõpetaja Peter Osse. 1881. aasta suvel määrati õppenõukogus põhiaineteks matemaatika, vene keel, joonistamine, geograafia, prantsuse keel, saksa keel ja loodusteadused. Esimesel aastal võeti õpilasi vastu vaid teise ning kolmandasse klassi, järgmisel aastal tuli juurde neljas klass, kus lisandusid õppeainetena füüsika ja inglise keel. Seoses venestuspoliitikaga hakati alates 1886. a jaanuarist õpetama märkimisväärselt rohkem vene keeles. 1883. aastal valmis arhitektide Max Hoeppeneri ja Carl Jacoby projekteeritud uus koolihoone, mida kasutatakse tänaseni. Kuni selle ajani üüris kool ruume vanalinnas Laial tänaval. 1885. aastal lõpetas esimene lend kuue õpilasega. Selle lennu vilistlane on esimene eestlasest realist Mihkel Vitsut.',
            '1890-1918': '19. sajandi viimasel kümnendil alustas tsaar Aleksander III venestuspoliitikat, mille eesmärgiks oli kõigi impeeriumi rahvaste ühtseks assimileerimine. Selle tõttu muudeti 1890. aastal kooli nimi ümber Revelskoje Petrovskoje Utšilišeks. Vene õppekeelele üleminekuga venitati, kuid 1890. aastal sai see siiski teoks. Aasta varem määrati kooli uueks direktoriks Wilhelm Petersen, kes oli ametis 1915. aastani, mis teeb temast kõige kauem ametis olnud Reaalkooli direktori. Koolivormi moodustasid must kuub, nahkrihm kullatud plaadiga ning must oranži kandiga müts, ees kuldsed ristatud tammelehed tähtedega ,,РПУ”. 1905. aasta revolutsiooni mõjutusena suurenes Reaalkooli õpilaste poliitiline aktiivsus. Võeti osa tööliste suurstreikidest ning pandi alus salarühmitusele Kommuuna. Vabatahtliku ainena hakati 1906. aastal õpetama eesti keelt. 1918. aastal jagunes Peetri Reaalkool kaheks – Eesti Reaalgümnaasiumiks ja Saksa Reaalgümnaasiumiks. Reaalkoolis oli populaarne ka huvitegevus, koolil oli oma orkester, õpilaskoor, võimlemisrühm, jalgpallimeeskond, vehklemisklubi ning maadlusring, kust sirgus Eesti kuulsamaid maadlejaid Georg Lurich.',
            '1918-1920': 'Veebruarirevolutsiooni järel moodustas Anton Õunapuu õpilastest üksuse, kellele ta andis sõjalist algõpetust. Just Õppiva Noorsoo Roodust sai korrakaitseüksus, mis valvas 24. veebruaril 1918 Tallinnas strateegilisi punkte. Tänu neile õpilastele saadi samal päeval välja kuulutada Eesti Vabariik. Juba järgmisel päeval saabunud saksa okupatsiooniga läks ÕNR põranda alla. 28. novembril algas Narva all Eesti Vabadussõda. Algushetkedel moodustasid õpilased ¼ Eesti kaitsevõimest, nendest 120 oli Tallinnast ja 80 Narvast. Kõige rohkem realiste sõdis Soomusrongil nr 2. Palju õppursõdureid sõdis ka Kalevlaste Malevas, mille üheks asutajaks oli legendaarne õpetaja Õunapuu. Reaalkoolist läks Vabadussõtta umbes 100 inimest. Kodumaa eest andis elu neli õpilast ja õpetaja Anton Õunapuu. 1923. aastal pandi aulasse langenute auks marmortahvel ja 1927 avati Reaalkooli ees mälestusmärk Vabadussõjas langenud õpetajatele ja õpilastele ehk Reaali Poiss.',
            '1921-1940': 'Eesti aeg oli Reaalkoolile arenguks soodne aeg. Sellel ajal kujunesid välja paljud tähtsad põhimõtted, traditsioonid ja sümbolid. 1921. aastal disainis Reaali joonistusõpetaja R. Nyman koolimütsi, mida kasutatakse tänaseni. Kuus aastat hiljem ehk 1927 valmis mälestusmärk Vabadussõjas langenud õpilastele ja õpetajatele ehk Reaali Poisi kuju. 1939. aastast pärineb Reaali hümn, millele kirjutas sõnad vil!54 Ilmar Mikiver. Ajastu legendaarsemad õpetajad olid direktor Nikolai Kann, füüsika-matemaatika õpetaja Paul Ederberg (Pudi), kellest sai alguse pudireas käimise traditsioon, ning inspektor Ernst Peterson Särgava (Habe), kellest eredalt mäletatakse tema kommet pidada poistele „mäejutlusi”. Tunnivälisel ajal oli au sees ka musitseerimine ning 1919. aastal loodud Reaali puhkpilliorkestrit peeti 1925. aastal lausa Tallinna parimaks. Peale selle olid realistide seas populaarsed võrkpall ning korvpall. Mõlemal alal saavutati häid tulemusi ning võrkpallis suudeti meistritiitlit kaitsta tervelt 13 aastat.',
            '1941-1950': '1944. aastaks oli võitlustanner taas Eestisse jõudnud. 9. ja 10. märtsil toimus Nõukogude Liidu suurim õhurünnak Tallinnale, mille tagajärjel ligi kolmandik linnast purustati ja põletati. Kannatada sai ka Tallinna Reaalkool. Poiss aga püsis täiesti tervena 1948. aasta kevadeni, mil kommunistid selle hävitasid. 16. oktoobril 1944 algas ümbernimetatud Tallinna 2. Keskkoolis taas õppetöö, mis oli katkenud märtsipommitamise tõttu. Muutliku aja tõttu ei jäänud kooli etteotsa ükski direktor kauaks. Neljakümnendatel jõudis ametis olla viis direktorit, kuni lõpuks 1949.aastal EmiliePertelsjäi pikemaks perioodiks sellele kohale. Rahulikku koolielu segas ka aktiivne Nõukogude propaganda, õpilaste arreteerimised ning 1949. aasta küüditamine, mille käigus viidi minema ka paar Reaalkooli poissi. Uue korraga keelati koolisõrmused ja (mitteametlikud) lõpumärgid, kuid iga lend tegi neid siiski salaja. Aktiivne tunniväline elu oli väheseid asju, mis kommunismi tulekuga ei kadunud. Populaarsemad huviringid olid endiselt sport ja muusika. Tegeleti pallimängude, male-kabe, ujumise ning vehklemisega. Muusikaringi koosseisu kuulusid meeskoor, ansamblid, puhkpilliorkester ja tantsuorkester.',
            '1951-1960': 'Tallinna 2. Keskkool oli üheteistkümneklassiline ning õpilaste arv koolis kasvas kiiresti: kümnendi alguses oli koolis õpilasi üle 900, teises pooles aga juba üle tuhande. Süveneva ruumipuuduse lahendamiseks lammutati kooli juures olev kõlakoda ning 1957. aastal alustati väikese maja ehitustöödega, mis lõpetati 1958. aastal. Kuigi 1950. aastatel toimus õppimine koolis riigi poliitilise ideoloogia alusel, oli elu siiski rahulikumaks muutunud. Taas kujunesid välja kuulsusrikkad õpetajad ning alguse sai nii mõnigi tänaseni kestev traditsioon. Ajastu tuntumad õpetajad on keemia- ja looduslooõpetaja Linda Visnapuu, joonestusõpetaja Voldemar Vahar ja muusikaõpetaja Voldemar Tomingas. 1952. aasta kevadel pani direktor EmiliePertels alguse lõpukella traditsioonile, 1956. aastast alates on peetud vilistlasõhtuid. Oluline muudatus koolielus toimus koolielus 1954. aastal, sest siis muudeti põline poistekoolsegakooliks.',
            '1961-1970': 'Nii nagu igal ajastul, kujunesid ka 1960. aastatel õpilastel oma lemmikõpetajad. Kõige eredamalt on sellest ajast jäänud õpilastele meelde direktor Aleksei Tsõgankov ehk Paša. Vaatamata sellele, et ta pandi ametisse, kuna tal polnud varasemat kokkupuudet Reaaliga, sai temast kiiresti kooli patrioot ning mees, kes oli kooli kuulsuse nimel valmis ette võtma kõikvõimalikke üritusi. Lisaks kontrollis ta isiklikult iga päev, et õpilased kannaksid korrektset koolivormi. Peamine klassiväline tegevus koondus 1960. aastatel kunstihuviliste klubi ja tehnikahuviliste klubi alla. Kooli juhtkonna jaoks oli väga tähtis ka õpilaste poliitorganisatsioonidesse kuulumine, sest pioneeride ja komnoorte arv näitas kooli kvaliteeti. Komsomoli astuti lausa klasside kaupa. Väga populaarne komsomoli- ja pioneeritöö oli vanapaberi ja vanaraua kogumine, milles peeti isegi üleliidulisi võistlusi. Loomulikult oli endiselt au sees sport. Reaalkooli kehakultuurikollektiiv kandis 1950. aastatest Georg Lurichi nime ning sellesse kuulusid vabatahtlikult kõik 4.-11. klassi õpilased. Toimusid spordipäevad, klassidevahelised spartakiaadid, kooli parimate sportlaste valimised ning sõprusvõistlused naaberkoolidega. Kõikide nende ürituste üheks eestvedajaks oli kehalise kasvatuse õpetaja Aleksander Prikk, kelle auks kutsutakse alates 2012. aastast vilistlaspäeva spordivõistlust nimega Grand Prikk ning kes jäi Reaaliga seotuks oma elu lõpuni. Reaalkoolis tegeleti aktiivselt ka muusikaga, tegutsesid puhkpilliorkester, segakoor, tantsuorkester ja mitmesugused laulugrupid, sealhulgas ka topeltkvartetid. Ühest sellisest topeltkvartetist kujunes 1963. aastal ansambel Real, millega esineti koolipidudel, klubides ja asutuste süldipidudel. Bänd tegutses kuni 1972. aasta sügiseni.',
            '1971-1980': '1970. aastal andis Aleksei Tsõgankov kooli juhtimise üle Oskar Radikule. 1971. aastal avati Reaalkooli hoone kõrval Georg Lurichi bareljeef. Aastal 1975 mindi üle kohustuslikule 11-klassilisele keskharidusele ning õpetamine hakkas toimuma kabinetisüsteemis. Radiku eestvedamisel loodi Tallinna 2. Keskkooli ka spordikallakuga eriklassid, mis koosnesid silmapaistvatest ujujatest ning kergejõustiklastest. 1976. sai koolijuhiks esinduslik füüsikaõpetaja Hain Hiieaas, tänu kellele olid õpetajad säästetud mitmetest parteikomitee kummalistest käskudest. Alates Hiieaasa direktoriks olemise aastatest hakati õpilasi Reaalkooli vastu võtma konkursi alusel. Tunnivälise tegevuse kõrghetkedeks olid 1978-1979 inglise keele õpetaja Vivika Miti eestvedamisel lavastatud ülimenukad muusikalid „Minu veetlev leedi“ ja „Mary Poppins“. Traditsioone tähistati sarnaselt tänapäevaga, kuid mõningad muudatused on siiski toimunud. Lõpukella tähistati rahvariieteta ning tihti käidi ilusa ilmaga päev varem Roccaal Mares. Tol ajal peeti abiturientide balle igas linnarajoonis, Lenini rajooni oma Salme kultuurikeskuses, kuid Reaali õpilased otsustasid korraldada eraldi balli ka Tallinna 2. Keskkoolis. Lõpumärgi saamise traditsioon on püsinud peaaegu muutumatuna, vaid märk on muutunud. Enam ei ole märgil kujutatud tõrvikut, kuid märgi kuju on säilinud. Aulas olnud Lenini bareljeef kaeti märgiaktusel kangaga. 1970. aastate lõpus loodi ka Tallinna Reaalkooli Vilistlaskogu. Vilistlaskond on õppurkonnale eeskujuks, seisab kooli au eest ning suhtub lugupidamisega Reaalkooli sümboolikasse.',
            '1981-1990': '1980. aastatel ei tekkinud Tallinna 2. Keskkoolis uusi traditsioone, aga olemasolevate tähistamine muutus vabamaks. 1982. aastal mindi lõpukellale koolivormi asemel rahvariietes, mis oli midagi enneolematut - linnas ringi joostes tegid turistid pilti ja trammid peatusid, et abituriente vaadata. Külastati ka Reaali Poisi endist asukohta, kuhu viidi lilli ja väikeseid pilte, mille hiljem õpetajad kokku korjasid, et pahandusi ei tekiks. 1981. aasta oli eriline Reaalkooli jaoks, sest täitus 100 aastat kooli asutamisest. Selle puhul peeti Estonia kontserdisaalis suur juubeliaktus. Lisaks sellele toimus 25. septembril koolis juubelikontsert vilistlastega ning novembris võtsid Tallinna 2., Pärnu 2., Riia 2., ja Vilniuse 2. Keskkool mõõtu korvpallis ja võrkpallis. Reaalkooli poisid ja tüdrukud olid mõlemal alal kõige edukamad.',
            '1991-': 'Taasiseseisvumine tõi suuri muutusi nii Eestile kui Reaalile. Mitmed keelatud traditsioonid taastati ja loodi mitmeid uusi. 1990. aastal muudeti kooli nimi Tallinna Reaalkooliks. Sama aasta kevadel taaspaigaldati aulasse marmortahvel. 1993. aastal avati ametlikult uus Poisi kuju. Lõpumärgil IIK kujutis muutus R-täheks 1990. aastal ning 2001. aastal muutus märgi kujundus selliseks, nagu see oli enne Teist maailmasõda. Uue traditsioonina on alates 1995. aastast juurdunud rebaste ristimine. 2000. aastast pärineb Reaalis veel üks uus traditsioon – sõita terve gümnaasiumiga teatrisse. Väga oluliseks sündmuseks Reaali kooliaastakalendris on saanud kooli sünnipäeva tähistamine 29. septembril. Nagu alati Reaali ajaloos, leiavad reaalikad aktiivse õppimise kõrvalt aega ja tahtmist ka loomingu ning spordiga tegelemiseks ning teenivad oma tulemuste eest tunnustust nii Eestis kui välismaal.'
        }
        if request.POST.get('action-end'):
            time = round(t.time() - request.session['start-time'], 1)
            ctx = {
                'timedelta': time,
                'usertext': request.POST.get('usertext'),
                'text': request.session['test'],
                'score': spellcheck(request.POST.get('usertext'), request.session['test']),
                'speed': round(len(request.POST.get('usertext').split()) / time, 1)
            }
            return render(request, 'test/test.html', ctx)

        elif request.POST.get('action-start'):
            ctx = {
                'text': request.session['test'],
                'state': request.POST.get('action-start'),
                'maxlen': str(len(request.session['test'])),
                'writentext': '',
            }
            request.session['start-time'] = t.time()
            return render(request, 'test/test.html', ctx)
        
        elif request.POST.get('test-type'):
            ctx = {
                'text': tests.get(request.POST.get('test-type'))
            }
            request.session['test'] = tests.get(request.POST.get('test-type'))
            return render(request, 'test/test.html', ctx)
        
        else:
            return render(request, 'test/test.html')                
            
    else:
        return redirect('/login')