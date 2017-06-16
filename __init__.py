import random
import time
import ABVI
import ValueIterationAgent
import manage_AS
import mdp
import numpy as np
import excel_genrator
import mdp_DB_chineese
import ABVI_chineseDB
import Exact_chinese


#test the code here
#mp = mdp.MArkovDecisionProcess("2013-8")

#V = ValueIterationAgent.ValueIterationAgent(mp, discount= 0.9, iterations= 100)
#print "V", V

#abv = ABVI.abvi(mp, [0]*2)
#start_time = time.time()
#print abv.interactive_value_iteration(0.1, 10000)

#s = excel_genrator.excel_generator_db(1000)
#s.generate_worksheet()

#t = manage_AS.manage_AS()

#AS_list = t.get_AS_list()
#
# max_length = 0
# for ass in AS_list:
#     tempo =  t.get_CS(ass)
#     l = len(tempo)
#     if l > max_length:
#         max_length = l
#     print ass, ' = ', t.get_CS(ass)
#
# print 'maximum length', max_length


#t.merge_text("/Users/pegah/Documents/Research/Aomar/DataBase/chinese-DB/dataset2/rtdata.txt",
#             "/Users/pegah/Documents/Research/Aomar/DataBase/chinese-DB/dataset2/tpdata.txt")

#print t.get_qos(str(4111), str(13))

# t = mdp_DB_chineese.MDP_SEQ(2)
# AS = t.states
#
# print AS
#
# print t.getStartState()
#[u'4179', u'4180']
#print t.getTransitionStatesAndProbs('AS156', 4179, 'AS559')
#print t.getTransitionStatesAndProbs('AS156', 4179, 'AS1653')


# for i in xrange(len(AS)):
#     print AS[i]

#CSs = t.getPossibleCs("AS766")
# for i in xrange(len(tempo)):
#     print tempo[i]*2
#     print type(tempo[i])

# start = time.time()
# print t.getQoS_list("AS766", 2366, 0)
# finish = time.time()
#
# print 'elapsed time', finish-start
#
# print t.getQoS_list("AS766", 66, 0)

MDP = mdp_DB_chineese.MDP_SEQ(2)
MDP.fixStates()
states = MDP.states[0:3]

print 'sates', states

#abv = ABVI_chineseDB.abvi_chinese(_mdp = MDP, _states_list = states, _lambda =[0]*2, _discount=1.0, _height=2 )
#print abv.interactive_value_iteration()

abv = Exact_chinese.exact(_mdp= MDP, _states_list= states, _lambda= [0.2, 0.2], _discount= 1.0, _height= 2)
print abv.exact_value_iteraion()