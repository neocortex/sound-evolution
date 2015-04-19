import os

import csound_adapter
from genetics import Population
from instrument import Instrument

IMAGE_VIEWER = 'eog'
graph_filename = 'graph.jpg'
iterations = 0

print '\n*** SOUND-EVOLUTION ***\n\nPress\n\n[1]\tto run option "population"'\
      '\n[2]\tto run option "mutation"\n[3]\tto run option "make love"'

a = int(raw_input('\n:- '))


if a == 3:
    P = Population(4, Instrument, {'const_prob': 0.7, 'max_children': 3})
    while not raw_input('\nPress return to continue, anything else to quit:- '):
        for n, i in enumerate(P.individuals):
            try:
                print i.to_instr()
                print '\nPlaying Sound #{}'.format(n + 1)
                i.to_graph(graph_filename)
                os.system("%s %s &" % (IMAGE_VIEWER, graph_filename))
                csd = csound_adapter.CSD()
                csd.orchestra(i)
                csd.score('i 1 0 2')
                csd.play()
            except OSError:
                print '\nSkipping this iteration:- Csound crashed'
        n = int(raw_input(
            '\nWhich sound did you like best: 1, 2, 3 or 4?:- ')) - 1
        m = int(raw_input(
            'Which sound did you like 2nd best: 1, 2, 3 or 4?:- ')) - 1
        P.individuals[n].Fitness = 1
        P.individuals[m].Fitness = 1
        P.natural_selection(no_surviving=2)
        P.next_generation(0.0, 0.5)
        iterations += 1
        for i in P.individuals:
            i.Fitness = 0
        print 'Generation # {} has been created. Population size: {}'.format(
            iterations+1, len(P.individuals))

elif a == 2:
    P = Population(4, Instrument, {'const_prob': 0.7, 'max_children': 3})
    while not raw_input('\nPress return to continue, anything else to quit:- '):
        for n, i in enumerate(P.individuals):
            i.to_graph(graph_filename)
            print '\nPlaying Sound #{}'.format(n+1)
            os.system("%s %s" % (IMAGE_VIEWER, graph_filename))
            print i.to_instr()
            csd = csound_adapter.CSD()
            csd.orchestra(i)
            csd.score('i 1 0 2')
            csd.play()
        n = int(raw_input(
            '\nWhich sound did you like best: 1, 2, 3 or 4?:- ')) - 1
        P.individuals[n].Fitness = 1
        P.natural_selection(no_surviving=1)
        P.next_generation(1.0, 0.0)
        P.next_generation(1.0, 0.0)
        iterations = iterations+1
        for i in P.individuals:
            i.Fitness = 0
        print '\nMutating...Generation # {} has been created'.format(
            iterations + 1)

elif a == 1:
    P = Population(4, Instrument, {'const_prob': 0.7, 'max_children': 3})
    while not raw_input('\nPress return to continue, anything else to quit:- '):
        for n, i in enumerate(P.individuals):
            try:
                i.to_graph(graph_filename)
                print '\nPlaying Sound #{}'.format(n+1)
                os.system("%s %s" % (IMAGE_VIEWER, graph_filename))
                print i.to_instr()
                csd = csound_adapter.CSD()
                csd.orchestra(i)
                csd.score('i 1 0 5')
                csd.play()
            except OSError:
                print 'Skipping this iteration:- Csound crashed'
        n = int(raw_input(
            '\nWhich sound did you like best: 1, 2, 3 or 4?:- ')) - 1
        m = int(raw_input(
            'Which sound did you like 2nd best: 1, 2, 3 or 4?:- ')) - 1
        P.individuals[n].Fitness = 1
        P.individuals[m].Fitness = 1
        a = P.individuals[n]
        c = P.individuals[m]

        print "\nUpdating fitnesses.."
        P.natural_selection(no_surviving=2)
        print "Killing shitty individuals.."
        try:
            d = a.ficken(c)
        except:
            d = a.mutate()
        P.append_individual(d)
        print "There is lovin' goin' on.."
        print "There are now "+str((P.size))+" individuals.."
        b = a.mutate()
        P.append_individual(b)
        print "The fittest have mutated.."
        print "There are now " + str(P.size)+" individuals.."
        iterations = iterations+1
        print "Updating iterations.."
        for i in P.individuals:
            i.Fitness = 0
            print "Assigning fitnesses.."
        print 'Generation # {} has been created. Population size is {}'.format(
            iterations+1, len(P.individuals))

else:
    print "Dumbass, option unknown."

print 'Leaving Sound-Evolution...'
