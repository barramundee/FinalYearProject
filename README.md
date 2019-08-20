# Knight run

Advanced Maths and Game AI Coursework
Student: w1577152
Pedro Fernandes


# Abstract

“Knight Run” was a game development project in the ambit of the module Advanced Maths and Game AI, developed by Pedro Fernandes in his final year of University during 2019. The aim of the coursework was to develop a game environment that demonstrated a comprehension of a variety of game AI techniques for a proposed scenario and, this report, justifying the selected methodology implementation of this project. The module leader, Markos Mentzelopoulos, gave his students full creative freedom when developing this coursework, giving them only guidance on what they should focus on: random arena generation and enemy AI. Thus, this report firstly showcases Section 1 and Section 2 of the coursework guidelines, being a Maths exercise using Quaternions and Matrices, followed by a detailed representation of how the game was developed, what techniques were used, and an explanation on the behaviours of the enemies and how these were coded.


# Section 1 – Mathematics

## Question 1

q1=8-i+j+1k
q2=-6+i+4j-7k
Quaternion Product: (8 x -6) + (8 x 1)i + (8 x 4)j + (8-7)k + (-1 x -6)I + (-1 x 1)i2 + (-1 x 4)ij + (-1 x -7)ik + (1 x -6)j + (1x1)ji + (1 x 4)j2 + (1 x -7)jk + (1 x -6)k + (1 x 1)ki + (1 x 4)kj + (1 x -7)k2 = = -48 + 8i + 32j – 56k + 6i - i2 - 4ij + 7ik – 6j + ji + 4j2 – 7jk – 6k + ki + 4kj – 7k2 – 48 + 8i + 32j – 56k + 6i + 1 – 4k – 7j – 6j – k – 4 – 7i – 6k + j – 4i + 7 =
= -44 + 3i + 20j – 67k
Python code: import numpy as np def qmultiplication(quaternion1, quaternion2): w1, x1, y1, z1 = quaternion1 w2, x2, y2, z2 = quaternion2 w = w1*w2 - x1*x2 - y1*y2 - z1*z2 x = w1*x2 + x1*w2 + y1*z2 - z1*y2 y = w1*y2 + y1*w2 + z1*x2 - x1*z2 z = w1*z2 + z1*w2 + x1*y2 - y1*x2 return np.array([w, x, y, z]) q1 = 8, -1, 1, 1 q2 = -6, 1, 4, -7 finalanswer = qmultiplication(q1, q2) print(finalanswer)
Quaternion Quotient:
(8 + i + j + k ) ∗ (6 – i – 4j + 7k)(6+ i+ 4j− 7k)∗ (6 – I – 4j + 7k)
= 48 – 8i – 32j + 56k – i2 – 4ji – 7ki + 6i + 6j – ij – 4j2+ 7kj + 6k – ik – 4jk + 7k236−6𝑖−24𝑗+42𝑘−𝑖2+6𝑖−4𝑗𝑖+7𝑘𝑖+24𝑗+4𝑗𝑖−16𝑗2−28𝑗𝑘−42𝑘+7𝑘𝑖+28𝑘𝑗−49𝑘2
= 48 – 8i – 32j + 56k+1+ 4k – 7j + 6i + 6j – k+ 4− 7i + 6k+j – 4i−736−6𝑖−24𝑗+42𝑘+1+6𝑖+4𝑘+7𝑗+24𝑗+4𝑘+16−28𝑖−42𝑘−7𝑗−28𝑖+49
= −52+9𝑖−32𝑗+ 55𝑘102

Python code:
import numpy as np def quotient(quaternion1, quaternion2): q2_conjugated = np.array(quaternion2) * np.array([1.0, -1, -1, -1]) # quaternion1 * q2_conjugated / quaternion2 * q2_conjugated w1, x1, y1, z1 = quaternion1 w2, x2, y2, z2 = q2_conjugated w3, x3, y3, z3 = quaternion2 w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2 x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2 y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2 z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2 a = w3 * w2 - x3 * x2 - y3 * y2 - z3 * z2 b = w3 * x2 + x3 * w2 + y3 * z2 - z3 * y2 c = w3 * y2 + y3 * w2 + z3 * x2 - x3 * z2 d = w3 * z2 + z3 * w2 + x3 * y2 - y3 * x2 return w, x, y, z, a, b, c, d q1 = 8, -1, 1, 1 q2 = -6, 1, 4, -7 q = quotient(q1, q2) print(q)

## Question 2

x1 – 2 + x3 = 1
8x1 + 3x2 – 2x3 = 0
5x1 + 5x2 + 2x3 = 1
101𝟖32552 = 301
R2 – 8R1 -> R2 
1x8 = 8 0x8 = 0 1x8 = 8 3x9 = 24
8 – 8 = 0 3 – 0 = 3 -2 – 8 = 10 0 – 24 = -24
101𝟎3−10𝟓52 = 3−241
R3 – 5R1 -> R2 
1x5 = 5 0x5=0 1x5=5 3x5=15
5 – 5 = 0 5 – 0 = 5 2 – 5 = 3 1 – 15 = -14
101𝟎𝟑−10𝟎5−3 = 3−24−14
13R2 -> R2 
0 x 13 = 0 3 x 13 = 1 -10 x 13 = 103 -24 x 13 = -8
101𝟎𝟏103𝟎𝟓−3 = 3−8−14
R2 - 5R2 -> R3 
0 x 5 = 0 1 x 5 = 5 - 103 x 5 = - 503 - 8 x 5 = - 40
0 – 0 = 0 5 – 5 = 0 -3 - 503 = 413 -14 – (-20) = 26
101𝟎𝟏103𝟎𝟎𝟒𝟏𝟑 = 3−826
341 R3 -> R3 
0 x 341= 0 0 x 341 = 0 341 x 413 = 1 26 x 341 = 7841
10𝟏𝟎𝟏103𝟎𝟎1 = 3−87841
R1 - R3 -> R1 
1 - 0 = 1 0 – 0 = 0 1 – 1 = 0 3 - 7841 = 4541
10𝟎𝟎𝟏𝟏𝟎𝟑𝟎𝟎1 = 4541−87841
R2 + 103R3 -> R2 
0 x 103 = 0 = 0 0 x 103 = 0 1 x 103 = 103 7841 x 103 = 26041
0 + 0 = 0 1 + 0 = 1 - 103 + 103 = 0 - 8 + 26041 = - 6841
10𝟎𝟎𝟏𝟎𝟎𝟎1 = 4541−68417841
x1 = 𝟒𝟓𝟒𝟏
x2 =−𝟔𝟖𝟒𝟏
x3 =𝟕𝟖𝟒𝟏

Python code: MAX = 100 def LUDecomposition(matrix, n): lower = [[0 for x in range(n)] for y in range(n)] upper = [[0 for x in range(n)] for y in range(n)] for i in range(n): for k in range(i, n): sum = 0 for j in range(i): sum += (lower[i][j] * upper[j][k]) upper[i][k] = matrix[i][k] - sum for k in range(i, n): if (i == k): lower[i][i] = 1 else: sum = 0 for j in range(i):
sum += (lower[k][j] * upper[j][i]) lower[k][i] = int((matrix[k][i] - sum) / upper[i][i]) print("Lower Triangular\t\tUpper Triangular") for i in range(n): for j in range(n): print(lower[i][j], end="\t") print("", end="\t\t\t") for j in range(n): print(upper[i][j], end = "\t") print("") matrix = [[1, 0, 1], [8, 3, -2], [5, 5, 2]] LUDecomposition(matrix, 3)
Determinant: def determinant(matrix): n = len(matrix) if n > 2: unit = 1 x = 0 sum = 0 while x <= n - 1: set = {} t1 = 1 while t1 <= n - 1: m = 0 set[t1] = [] while m <= n - 1: if m == x: u = 0 else: set[t1].append(matrix[t1][m]) m += 1 t1 += 1 l1 = [set[x] for x in set] sum = sum+unit*(matrix[0][x])*(determinant(l1)) unit = unit * (-1) x += 1 return sum else: return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0] answer = determinant([[1, -3, 7], [-2, 6, 1], [0, 3, -2]]) print(answer)


# Section 2 – Random arena generation


The Knight finds himself in the cursed Arena, product of the evil Necromancer – he is unable to escape it until he defeats all of the Necromancer minions and, should he fail, he’s brought back to the beginning of the same Arena, in an endless loop. However, each time the Knight is brought back, the Arena seems slightly different to him… This is because the Necromancer has cursed the Arena with a Random Obstacle Generator script that, at the start of each game’s code run, distributes an Array of obstacles throughout the playable area of the Arena! Let’s take a look at the obstacles present in the Arena:

## 2.1 - Obstacles:

Brick Block: This block serves two main functions. The most important one is the fact that it serves as a main outliner, unbreakable block around the arena that the Knight cannot cross. For this, a Box Collider 2D was used, and it was placed around the Arena in a square formation. The second use for this block is as a main obstacle for the Arena, but with slightly different properties: should the Knight hit this block with his melee attack, there is a one in six chance that the block will drop a health potion, replenishing the Knight’s health by one heart. It is also extremely fragile, easily breaking when Enemies run towards it – note that it may only drop Health Potions when broken by the Knight’s hammer. When the algorithm is running, per walkable grid space, there is a 1 in 100 chance of spawning this type of obstacle.
Spikes: Spikes are a hazardous obstacle that spawn throughout the arena that damage both the Knight and Enemies when stepped upon. This was done by adding a Box Collider 2D to Spikes that have a Trigger that reduces an entity’s health points by one heart whenever it enters its edge radius. Spikes can also be destroyed by the Knight’s hammer, although they’re so small it might be difficult to hit them sometimes – the strategy should be to lure enemies into Spikes to cause extra damage to them. Similar to the Brick Block, the spikes also have a 1 in 100 chance of spawning per walkable grid space – too many spikes would prove to be too annoying for any randomly generated arena, as I wanted the game to have a feel of freedom to run around and dodge enemy projectiles.
Skeleton Remains: Although they may look harmless at first, the Knight should tread carefully when stepping on these –they’re actually sleeping Skeletons! Entering the edge of this Obstacle’s Box Collider 2D will instantiate a Skeleton Enemy on the spot, removing the Remains from the Arena. Similar to both the Brick Blocks and the Spikes, the Skeleton Remains also have a 1 in 100 chance of spawning.
Health Potion: Health Potions have a 1 in 6 chance of spawning when blocks are broken by the Knight’s hammer, but they also spawn periodically and randomly throughout the Arena’s playable grid after one minute has passed in the game. They share similar code to the Spikes’ Script, but instead of damaging entities that walk over them, they only interact with entities with the tag “Player” and heals them instead by one heart.
Monster Spawners: While they’re not interactive from the Knight’s perspective, Monster Spawners play an important part in the gameplay of Knight Run – periodically, these random points spawn either Zombies, Demons or Skeletons into the Arena, by randomizing a position in the playable grid of the Arena and then instantiating the entities (similar to how Health Potions are also instantiated into the arena).

## 2.2 - Generation Algorithm

The Arena Generation is relativity simple: a grid point is selected in the middle of the arena, that can either be transformed Left, Right, Up or Down (as this is a 2D game). For each movement, that point will instantiate either an Empty block, a Brick Block or a Skeleton Remain (only one object might be instantiated per grid block). This point will move and instantiate a block an x max number of times, and should he pass through a block that already has a block instantiated, he will add +1 to his x max number of blocks instantiated (this makes it so that a specific number of objects is always instantiated). It also means that all the obstacles in the map have no order / specific position they can be instantiated in, meaning that each play through the arena is completely randomized (no Obstacles are pre-defined in the arena, all of them are generated randomly at the beginning of the game’s execution).
public class RandomGeneratorRemastered : MonoBehaviour
{
public int enemyAmount = 10;
public GameObject[] tiles;
public List<Vector3> createdTiles;
public int numberOfTiles;
public int tileSize;
public float waitTime;
public float upProbability;
public float rightprobability;
public float downProbability;
//walls
public float minY;
public float maxY;
public float minX;
public float maxX;
private float minXSpawn = 586;
private float minYSpawn = -90;
private float maxXSpawn = 745;
private float maxYSpawn = 50;
public float xNumber;
public float yNumber;
void Start()
{
//SoundManager.PlaySound("theme");
StartCoroutine(GenerateArena());
}
IEnumerator GenerateArena()
{
for (int i = 0; i < numberOfTiles; i++)
{
float direction = Random.Range(0f, 1f);
int tile = Random.Range(0, tiles.Length);
CreateTile(tile);
CallMoveGenerator(direction);
//yield return new WaitForSeconds(waitTime);
}
yield return 0;
}
void CallMoveGenerator(float random)
{
if (random < upProbability)
{
MoveGenerator(0);
}
else if (random < rightprobability)
{
MoveGenerator(1);
}
else if (random < downProbability)
{
MoveGenerator(2);
}
else
{
MoveGenerator(3);
}
}
//&& !createdTiles.Contains(new Vector3(transform.position.x, transform.position.y + tileSize, 0))
void MoveGenerator(int direction)
{
switch (direction)
{
case 0:
if (transform.position.y + tileSize < maxY)
{
transform.position = new Vector3(transform.position.x, transform.position.y + tileSize, 0);
} else
{
numberOfTiles++;
}
break;
case 1:
if (transform.position.x + tileSize < maxX)
{
transform.position = new Vector3(transform.position.x + tileSize, transform.position.y, 0);
} else
{
numberOfTiles++;
}
break;
case 2:
if (transform.position.y - tileSize > minY)
{
transform.position = new Vector3(transform.position.x, transform.position.y - tileSize, 0);
} else
{
numberOfTiles++;
}
break;
case 3:
if (transform.position.x + tileSize > minX)
{
transform.position = new Vector3(transform.position.x - tileSize, transform.position.y, 0);
} else
{
numberOfTiles++;
}
break;
}
}
void CreateTile(int tileIndex)
{
if (!createdTiles.Contains(transform.position) && !(transform.position.x > minXSpawn && transform.position.x < maxXSpawn && transform.position.y > minYSpawn && transform.position.x > maxYSpawn))
{
GameObject tileObject;
tileObject = Instantiate(tiles[tileIndex], transform.position, transform.rotation) as GameObject;
createdTiles.Add(tileObject.transform.position);
}
else
{
numberOfTiles++;
}
}
}
  
# Section 3 – Player and Enemies

## 3.1 – The Player

Knight: In Knight Run, you play as a swift Knight (moved around by pressing the WASD Keys) wielding both a Throwing Axe (by pressing Mouse 2 and aiming in the desired direction), which has a 1 in 10 chance of becoming a faster, wider and stronger version of itself, as well as a melee hammer (by pressing Mouse 1) that might destroy some obstacles in the Arena. The Knight also has 5 health hearts that are depleted if he gets into contact with hazardous obstacles in the Arena, Enemies or Enemy projectiles - these hearts can be replenished by collecting health potions scattered throughout the Arena. The Knight’s objective is to kill the final boss of the Arena that spawns after he has killed 25 enemies.

## 3.2 – The Enemies

As part of this coursework’s specification, each Enemy was designed with a specific behaviour in mind, with the player immediately recognising its pattern just by looking at it. Although 3 enemies were required, for this game 5 different enemies were coded, to add variety to the gameplay.

### Zombie

The Zombie was the first enemy that was designed and implemented into the Arena. He’s the Enemy with the highest base speed (faster than the Knight’s!) when he spawns, as well as the highest health pool (6 full hearts). As soon as the Zombie is spawned into the Arena, he gets the Knight’s position and starts running frantically towards him, without regard for any Obstacles in his way – however, if he runs into an Obstacle, he takes both damage as well as destroying the Object in his path. Should he manage to run into the Knight, he will explode and damage the Knight by 1 heart as well as killing himself in the process. But there’s a catch: the more damage the Zombie takes, the slower he becomes. When the Zombie gets below 3 Health, instead of running towards the Knight, he will run towards the Necromancer, who is placed at the northernmost side of the arena. Should he get into range of him, the Necromancer will heal the Zombie until full health, at which point he will start running towards the Knight again!

### Demon

The Demon is a ranged threat that spawns in the Arena at the same rate as the Zombie. He has a medium health pool (4 full hearts) as well as having around the same movement speed of the Zombie when he is half-damaged. The Demon’s behaviour is an interesting one: he will shoot Fireballs that deal 1 heart of damage from any distance towards the Knight, while simultaneously running towards him. However, Demons would rather not get too close to the Knight, so they will always keep a static amount of distance between them and the Knight. Should the player approach these demons to try to fight them in close range, they will be in bad luck – as fast as the demons approach the Knight, they will also retreat should the Knight get too close to them. A situation the player does not want to find himself in is being cornered by a swarm of Demons, as an escape will be unlikely!

### Skeleton

Skeletons are shy enemies that tend to avoid trouble most of the time. They are relatively weak when compared to the other Enemies (3 full hearts), and have the lowest speed out of all of them. Although they spawn less regularly than the other Enemies (only when the Knight steps onto a Skeleton Remain object or every 15 seconds), the Skeleton will patrol the Arena from a random amount of array points, randomly selected every 3-5 seconds. They will not target the Knight or interact with him unless the Knight comes into the Skeleton’s field of view, which will result in the skeleton becoming heavily enraged and attacking the Knight with a barrage of ranged projectiles. Furthermore, after multiple Skeletons have spawned, they will start patrolling the map together, becoming a bigger swarm of enemies as time passes. Don’t wake them up!

### Necromancer

The Necromancer is the mastermind behind the Arena – as a result, he plays only a passive part in the Arena’s gameplay, being fully untargetable and invulnerable. The Necromancer will only perform actions when there is a Zombie with low health within his vicinity. When this happens, he will shoot friendly projectiles towards him that will heal the Zombie for 1 heart at a time. However, when the player reaches 25 kills, the Necromancer will unleash his most dangerous creation, a massive ogre with an enormous health pool that attempt to kill the Knight as soon as he spawns onto the Arena.

### Ogre

The Ogre should be the Knight’s biggest nightmare, as he has the largest Health Pool by far (about 100 hearts). He will follow the Knight around while shooting massive projectiles at him. He is the slowest enemy by far, with also the lowest fire rate of projectiles. He makes up for this, however, by being extremely bulky and hard to kill. Once he has been defeated, the Knight will be greeted with a Game Won screen!

# Section 4 - Conclusion

Knight Run was an overall fun game idea to develop, inspired by indie games such as “Binding of Isaac” and “Enter the Gungeon”. Both of those mentioned games are fast paced, with enemies that have easily identifiable attack patterns, something that I wanted to really emphasize on this coursework. The random arena generation might also not be the most robust or advanced, but an earlier arena generation algorithm was tested and it proved to remove the game’s essence if the arena was fully randomly generated – what happened was that with a complete random arena (with randomly generated corridors and end points), it removed the sort of free-running feel, where you could run around and dodge enemy projectiles easily without being restricted by the arena’s layout. Furthermore, a lot of effort was made to polish the game’s visuals to the best – I am a big fan of pixel art and 2D games so this was an amazing opportunity for me to develop my skills. As this was my first game development project, I am overall very pleased with the end result. Although throughout my Software Engineering degree in University I have been pleased with my module choices, Advanced Maths and Game AI made me wish I had picked a Games Development module earlier in my career.

# Appendixes

Demo Video: https://www.youtube.com/watch?v=VZmMw0IeH28
GeeksforGeeks. (2019). Determinant of a Matrix - GeeksforGeeks. [online] Available at: https://www.geeksforgeeks.org/determinant-of-a-matrix/ [Accessed 24 March 2019].
GeeksforGeeks. (2019). Doolittle Algorithm : LU Decomposition - GeeksforGeeks. [online] Available at: https://www.geeksforgeeks.org/doolittle-algorithm-lu-decomposition/ [Accessed 24 March 2019].
GeeksforGeeks. (2019). Printing brackets in Matrix Chain Multiplication Problem - GeeksforGeeks. [online] Available at: https://www.geeksforgeeks.org/printing-brackets-matrix-chain-multiplication-problem/ [Accessed 6 April 2019].
GeeksforGeeks. (2019). Program for quotient and remainder of big number - GeeksforGeeks. [online] Available at: https://www.geeksforgeeks.org/program-quotient-remainder-big-number/ [Accessed 12 May 2019].
itch.io. (2019). Top game assets. [online] Available at: https://itch.io/game-assets [Accessed 24 March 2019].
Unity. (2019). Top Down 2D Game Basics - Unity. [online] Available at: https://unity3d.com/learn/tutorials/topics/2d-game-creation/top-down-2d-game-basics [Accessed 6 April 2019].
Unity. (2019). 2D Roguelike tutorial - Unity. [online] Available at: https://unity3d.com/learn/tutorials/s/2d-roguelike-tutorial [Accessed 14 March 2019].
YouTube. (2019). Live Training: Top Down 2D Games. [online] Available at: https://www.youtube.com/watch?v=uv2QSvuwIDs&t=2866s [Accessed 6 April 2019].
YouTube. (2019). Mini Unity Tutorial - How To Add Sound Effects. [online] Available at: https://www.youtube.com/watch?v=JnbDxG04i7c [Accessed 3 May 2019].
YouTube. (2019). PROCEDURAL TERRAIN in Unity! - Mesh Generation. [online] Available at: https://www.youtube.com/watch?v=64NblGkAabk [Accessed 14 March 2019].
YouTube. (2019). RANDOM DUNGEON GENERATION - EASY UNITY TUTORIAL - #2. [online] Available at: https://www.youtube.com/watch?v=eR74EjkA_4s [Accessed 14 March 2019].
YouTube. (2019). RANDOM DUNGEON GENERATOR - EASY UNITY TUTORIAL - #1. [online] Available at: https://www.youtube.com/watch?v=qAf9axsyijY&t=154s [Accessed 15 March 2019].
YouTube. (2019). Unity Top Down Shooter #1 - Player Movement & Look. [online] Available at: https://www.youtube.com/watch?v=lkDGk3TjsIE&t=1300s [Accessed 6 April 2019].
