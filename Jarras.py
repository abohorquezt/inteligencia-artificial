
# coding: utf-8

# In[4]:

import util
import search
class jars_problem(search.SearchProblem):
    #Definicion de variaables a usar.
    def __init__(self, initial, goal):
        self.initial = initial #Estado inicial
        self.goal = goal #Estado objetivo
        self.capacidadJ1 = 5 #Capacidad jarra1
        self.capacidadJ2 = 4 #Capacidad jarra2
    #Definicion de reglas o acciones a realizar.
    def actions(self, state):
        #Matriz con las acciones posibles.
        actions = ['vaciarJ1aJ2', 'vaciarJ2aJ1', 'vaciarJ1', 'vaciarJ2', 'llenarJ1', 'llenarJ2']
        return actions
    #Comportamiento de las acciones a realizar.
    def result(self, state, action):
        #Rutina para la accion de vaciar la jarra1 en la jarra2
        if action is 'vaciarJ1aJ2':
            cantidadJ1 = state[1]
            cantidadJ2 = state[3]
            j1 = 0
            j2 = 0
            diferenciaJ2 = self.capacidadJ2 - cantidadJ2

            if diferenciaJ2 > 0:

                if cantidadJ1 >= diferenciaJ2:
                    totalJ1 = cantidadJ1 - diferenciaJ2
                    cantidadADepositar = cantidadJ1 - totalJ1
                    j2 = cantidadJ2 + cantidadADepositar
                    j1 = totalJ1
                else:
                    j2 = cantidadJ1 + cantidadJ2
                    j1 = 0
                #Definición del estado en el que se encuentra cada jarra luego de haberse sometido a esta regla.
                state = ('Jarra 1', j1, 'Jarra 2', j2)
                return state
        #Rutina para la accion de vaciar la jarra2 en la jarra1 - elif es un if-else contraido.
        elif action is 'vaciarJ2aJ1':
            cantidadJ1 = state[1]
            cantidadJ2 = state[3]
            j1 = 0
            j2 = 0

            diferenciaJ1 = self.capacidadJ1 - cantidadJ1

            if diferenciaJ1 > 0:

                if cantidadJ2 > diferenciaJ1:
                    totalJ2 = cantidadJ2 - diferenciaJ1
                    cantidadADepositar = cantidadJ2 - totalJ2
                    j1 = cantidadJ1 + cantidadADepositar
                    j2 = totalJ2
                else:
                    j1 = cantidadJ2 + cantidadJ1
                    j2 = 0
                #Definición del estado en el que se encuentra cada jarra luego de haberse sometido a esta regla.
                state = ('Jarra 1', j1, 'Jarra 2', j2)
                return state
        #Rutina para la accion de vaciar la jarra1  - elif es un if-else contraido.
        elif action is 'vaciarJ1':
            j1 = 0
            #Definición del estado en el que se encuentra cada jarra luego de haberse sometido a esta regla.
            state = ('Jarra 1', j1, 'Jarra 2', state[3])
            return state
        #Rutina para la accion de vaciar la jarra2  - elif es un if-else contraido.
        elif action is 'vaciarJ2':
            j2 = 0
            #Definición del estado en el que se encuentra cada jarra luego de haberse sometido a esta regla.
            state = ('Jarra 1', state[1], 'Jarra 2', j2)
            return state
        #Rutina para la accion de llenar la jarra1  - elif es un if-else contraido.
        elif action is 'llenarJ1':
            j1 = self.capacidadJ1
            #Definición del estado en el que se encuentra cada jarra luego de haberse sometido a esta regla.
            state = ('Jarra 1', j1, 'Jarra 2', state[3])
            return state
        #Rutina para la accion de llenar la jarra2  - elif es un if-else contraido.
        elif action is 'llenarJ2':
            j2 = self.capacidadJ2
            #Definición del estado en el que se encuentra cada jarra luego de haberse sometido a esta regla.
            state = ('Jarra 1', state[1], 'Jarra 2', j2)
            return state
        
    def goal_test(self, state):
        return self.goal == state
    
    def path_cost(self, c, state1, action, state2):
        pass

    def value(self, state):
        pass
    
    def getStartState(self):
        return self.start


# In[5]:


def main():

    print("PROBLEMA DE LAS JARRAS")
    initial = ('Jarra 1', 0, 'Jarra 2', 0)
    goal = ('Jarra 1', 0, 'Jarra 2', 2)
    problem = jars_problem(initial, goal)
    #Busquedá de el estado objetivo dentro de las tuplas definidas
    result = search(problem)
    #Impresion del resultado y solución propuesta.
    print("RESULTADO")
    print(result)
    print("SOLUCION")
    print(result.solution())


# In[ ]:



