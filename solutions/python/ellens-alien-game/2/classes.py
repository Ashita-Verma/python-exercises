"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes:
        (class) total_aliens_created (int): Total number of Alien instances.
        x_coordinate (int): Position on the x-axis.
        y_coordinate (int): Position on the y-axis.
        health (int): Number of health points.

    Methods:
        hit(): Decrement Alien health by one point.
        is_alive(): Return a boolean for if Alien is alive (if health is > 0).
        teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
        collision_detection(other): Implementation TBD.

    """
    health = 3
    total_aliens_created = 0
    
    def __init__(self,cordinate_x, cordinate_y):
        """
        Initialize a new Alien instance with coordinates and track the total count.
    
        Parameters:
        cordinate_x (int): The starting x-coordinate of the alien on the grid.
        cordinate_y (int): The starting y-coordinate of the alien on the grid.
        """
        
        self.x_coordinate = cordinate_x
        self.y_coordinate = cordinate_y
        Alien.total_aliens_created += 1

    def hit(self):
        """
        Decrements the health of Alien
        """
        
        self.health -= 1 

    def is_alive(self):
        """
        Check if the alien has remaining health points.
    
        Returns:
        bool: True if health is greater than 0, False otherwise.
        """
        return self.health > 0

    def teleport(self, x_position, y_position):
        """
        Changes the co-ordinates of Alien
        
        Parameters:
        x_position (int): x-coordinate of new position.
        y_position (int): y-coordinate of new position.
        
        """
        
        self.x_coordinate = x_position
        self.y_coordinate = y_position

    def collision_detection(self, other_object):
        """
        collision detection algorithm when the Alien is hit.
        This function will be implemented in future.

        Parameters:
        other_object : To be defined later.
        """
        
        pass


#TODO (Student): Create the new_aliens_collection() function below to call your Alien class with a list of coordinates

def new_aliens_collection(alien_start_positions):
    return [Alien(x_pos,y_pos) for x_pos,y_pos in alien_start_positions]