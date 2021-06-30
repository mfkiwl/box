<p align="center">
  <img height="90" src="https://user-images.githubusercontent.com/8450091/123720914-cb9a5200-d84a-11eb-97d9-830776297b87.PNG"/>  
</p>

`box` is a text-based visual programming language inspired by Unreal Engine blueprint function graphs. 

```console
$ cat samples/factorial.box

 ┌─ƒ(Factorial)───┐                     ┌─[Branch]─────┐                       ┌─[Set]─┐
 │               ►┼─────────────────────┼►       True ►┼───────────────────────┼►     ►┼─────────┐         ┌─[For Loop]───────────┐                   ┌───────┐
 │             n ○┼──┐               ┌──┼○      False ►┼──┐  ┌──────────┐  ┌───┼○      │         └─────────┼►          Loop body ►┼───────────────────┼►      │
 └────────────────┘  │    ┌────────┐ │  │              │  │  │  result ○┼──┘ ┌─┼○      │                   │                      │ ┌──────────┐ ┌────┼○  *=  │
             ┌────┐  └────┼○  >=  ○┼─┘  └──────────────┘  │  └──────────┘    │ └───────┘         ┌────┐    │                      │ │  result ○┼─┘  ┌─┼○      │
             │ 1 ○┼───────┼○       │                      │       ┌────┐     │                   │ 1 ○┼────┼○ start               │ └──────────┘    │ └───────┘
             └────┘       └────────┘                      │       │ 1 ○┼─────┘                   └────┘    │                      │                 │
                                                          │       └────┘                                   │               index ○┼─────────────────┘
                                                          │                        ┌────┐                  │                      │
                                                          │                        │ n ○┼─┐  ┌───────┐     │                      │
                                                          │                        └────┘ └──┼○  +   │     │                      │
                                                          │                        ┌────┐ ┌──┼○     ○┼─────┼○ end                 │
                                                          │                        │ 1 ○┼─┘  └───────┘     │                      │
                                                          │                        └────┘                  │                      │
                                                          │                                      ┌────┐    │                      │
                                                          │   ┌─[Return]─┐                       │ 1 ○┼────┼○ step                │
                                                   ┌────┐ └───┼►         │                       └────┘    │           Completed ►┼────┐
                                                   │ 1 ○┼─────┼○         │                                 └──────────────────────┘    │  ┌─[Return]─┐
                                                   └────┘     └──────────┘                                               ┌─────────┐   └──┼►         │
                                                                                                                         │ result ○┼──────┼○         │
                                                                                                                         └─────────┘      └──────────┘
$ box samples/factorial.box -e 5
120

$ box samples/factorial.box -e 5
87178291200
```
