# MetaheuresticLearn
This package contain the implementation of various metaheurestic algorithms in python.

The main idea of this package is to provide a place for any one to start coding his own metaheurestic algorithm.

Simply, by instaling this package you will be able to write your algorithm by extending a specific class and adding yur logic.

Furthermore, this package will allow you to use some pre-implemented metaheurestic algorithm.


## Supported Platforms

* Python 2.7 and higher. 

## Required packages

* Numpy package
* Matplotlib package

## Available Algorithms

* Blackhole Algorithm

* Genetic Algorithm

Algorithms under construction:
* Many  other algorithms will be added soon


## Available  Functions
By implementing our `BaseAlgorithm` class, you will have the accecebility to the following functions:
* set_fitness_function(x) : used to identify the fitness function needed to evaluate the current soluction (should be minimization function) (required)
* set_error_function(x): used to identify the error of the best solution at the end of each epoch (optional).
* run() : used to start the optimization process[accept one parameter verbose=`boolean` to printing extra information while running]. This function return a dictionary as follows: 
  ```
        {
            'best': Any,
            'avg': Any,
            'worst': Any,
            'std': Any,
            'error': Any or None,
        }
  ``` 
* show_fitness_plot() : called after `run()` function to display a figure of the best fitness value at each epoch
* show_error_plot() : called after `run()` function to display a figure of the error value at each epoch

## Usage
### Configuration
To use any of the implemented algorithms, you need to identify at least the following:
* population (default is 100)
* iterations (default is 100)
* epochs (default is 1)
* boundaries: 2D array to identify the search space:
  ```
  bondaries = [
      [0,1], # first attribute boundaries
      [0,5] # second attribute boundaries
      .....
      [0,10] # nth attribute boundaries
  ]
  ```
  According to the previous array, we are searching for a value in a 3D space where the first dimension is between [0,1], the senond is between [0,5] and so on.
* fitness function: used to evaluate the  expected solutions. Has the following structure:
  ```
  def fitness(individual):
    //do your evaluation over the individual
    return `neumeric value`
  ```
* error function (optional): to evaluate the best solution's error after each epoch.  Has the following structure:
  ```
  def error(individual):
    //do your evaluation over the individual
    return `neumeric value`
  ``` 

### Implemented Algorithms
After performing the parameter configuration, you can call any of the implemeneted algorithms as follows:
```
optimizer = BlackHole(population=100, iterations=150, boundaries=ranges, epochs=2)

optimizer.set_fitness_function(fitness)
optimizer.set_error_function(error)
statistics = optimizer.run(verbose=True)
```
The algorithm may accept more paramteres according to the implementaton.

### Constract Your Algorithms
To constract yor metaheurestic algorithm, create a new class and extend the `BaseAlgorithm` class. Then use the functions provided by `BaseAlgorithm` to construct your logic.
```
class YourAlgorithm(BaseAlgorithm):

    def after_initialization(self):
        # do anything here
        pass


    def before_update(self, iteration):
        # do anything here
        pass

    def update_individual(self, individual):
        # do anything here
        return individual

    def after_update(self, iteration):
        # do anything here
        pass
 
```
You can also access the internal state of the algorithm at any stage of execution using the followings:
* best_individual()
* worst_individual()
* get_fitness(index): if index not provided, the function will return all the individual fitnesses
* get_individual(index): if index not provided, the function will return all the current population individual 
* set_individual(index,new_individual): to update individual at the specified index
* get_individual_length() to retrive length of any individual in the population.



## Contributing

Bug reports and pull requests are welcome on GitHub 

## License

The project is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
