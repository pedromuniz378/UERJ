function getAdjacencyMatrix(adjacencyList) {
    // Pega a Matriz de Adjacencias a partir da lista de adjacencias
    let A = []
    for (let i = 1; i <= Object.keys(adjacencyList).length; i++) {
        let row = []
        for (let j = 1; j <= Object.keys(adjacencyList).length; j++) {
            if (adjacencyList[i].includes(j)){
                row.push(adjacencyList[i].filter(v => v == j).length)
            } else{
                row.push(0)
            }
        }
        A.push(row)
    }
    return A
}

function warshallAlgorithm(adjacencyMatrix) {
    // Algoritmo de Warshall
    adjacencyMatrix = adjacencyMatrix.map(v => [...v])
    let len = adjacencyMatrix.length
    let operations = 0
    for (let k = 0; k < len; k++) {
        for (let j = 0; j < len; j++) {
            for (let i = 0; i < len; i++) {
                let bool = !!(adjacencyMatrix[i][j]) || (!!adjacencyMatrix[i][k] && !!adjacencyMatrix[k][j])
                operations = operations + 2
                adjacencyMatrix[i][j] = bool ? 1 : 0
            }
        }
    }
    return [adjacencyMatrix, operations]
}

function powerFormula(adjacencyMatrix) {
    // Fórmula de Potências
    adjacencyMatrix = adjacencyMatrix.map(v => [...v])
    let len = adjacencyMatrix.length
    let operations = 0

    let R = [adjacencyMatrix]
    for (let n = 1; n < len; n++) {
        let An = []
        for (let i = 0; i < len; i++) {
            let row = []
            for (let j = 0; j < len; j++) {
                let Aij = 0
                for (let k = 0; k < len; k++) {
                    if (n == 2) {
                        Aij = Aij || (adjacencyMatrix[i][k] && adjacencyMatrix[k][j])
                    } else {
                        Aij = Aij || (R[n-1][i][k] && adjacencyMatrix[k][j])
                    }
                    operations = operations + 2
                }
                row.push(Aij)
            }
            An.push(row)
        }
        R.push(An)
    }

    R = R.reduce((acc, curr) => {
        let newR = R.map(subMat => [...subMat])
        for (let i = 0; i < curr.length; i++){
            for (let j = 0; j < curr.length; j++)  {
                newR[i][j] = acc[i][j] || curr[i][j]
                operations++
            }
        }  
        return newR
    })

    return [R, operations]
}

function depthSearch(adjacencyMatrix, vertex, visited=[]) {
    // Busca em Profundidade

    // Pega todos os vértices adjacentes
    let adjacentToA = []
    adjacencyMatrix[vertex-1].forEach((v, i) => v ? adjacentToA.push(i+1) : null)

    // Visita um Vértice
    visited.push(vertex)

    // Reinicia o processopara um novo Vértice
    for (let n = 0; n < adjacentToA.length; n++) {
        if (!visited.includes(adjacentToA[n])) {
            depthSearch(adjacencyMatrix, adjacentToA[n], visited)
        }
        
    }
    return visited
}

class Queue {
    // Fila
    constructor() {
        this.queue = []
    }

    head() {
        if (this.queue.length > 0) return this.queue[0]
    }

    includesInQueue(el) {
        this.queue.push(el)
    }

    queueStrip() {
        return this.queue.shift()
    }

    isEmpty() {
        return this.queue.length == 0 ? true : false
    }
}

function widthSearch(adjacencyList, vertex, visited=[]) {
    // Busca em Largura
    let queue = new Queue

    // Visita um Vértice
    visited.push(vertex)
    queue.includesInQueue(vertex)

    while(!queue.isEmpty()) {
        // Pega todos os vértices adjacentes
        let adjacentToHead = []
        adjacencyList[queue.head() - 1].forEach((v, i) => v ? adjacentToHead.push(i + 1) : null)

        // Reinicia o processopara um novo Vértice
        for (let n = 0; n < adjacentToHead.length; n++) {
            if (!visited.includes(adjacentToHead[n])) {
                // Visita um Vértice
                visited.push(adjacentToHead[n])
                queue.includesInQueue(adjacentToHead[n])
            }
        }
        queue.queueStrip()
    }
    return visited
}

function amountOfVertexes(adjacencyMatrix) {
    // Conta a quantidade de Vértices
    return adjacencyMatrix.length
}
function amountOfArchs(adjacencyMatrix) {
    // Conta a quantidade de Arcos (arestas)
    return adjacencyMatrix.reduce((acc, curr) => {
        let currAmount = curr.reduce((acc, curr) => acc + curr)
        return acc + currAmount
    }, 0)
}

function howManyComeOut(adjacencyMatrix, vertex) {
    return adjacencyMatrix[vertex-1].reduce((acc, curr) => {
        return acc + curr
    }, 0)
}

function howManyComeIn(adjacencyMatrix, vertex) {
    return adjacencyMatrix.reduce((acc, curr) => {
        let comingIn = curr.reduce((acc, curr, idx) => idx == vertex-1 ? acc + curr : acc, 0)
        return acc + comingIn
    }, 0)
}

function getRoute(adjacencyList, reachabilityMatrix, vertex1, vertex2, ) {
    if (vertex1 == vertex1 && vertex2 == vertex2) {
        if (reachabilityMatrix[vertex1 - 1][vertex2 - 1] == 1) {
            return auxGetRoute(adjacencyList, vertex1, vertex2)
        } else {
            return false
        }
    } else return null



}

function auxGetRoute(adjacencyList, vertex1, vertex2, route=[]) {
    if (route.length == 0) route.push(vertex1)

    if (vertex1 == vertex2) return route

    let adjacent = adjacencyList[vertex1]
    for (let r = 0; r < adjacent.length; r++) {
        if (!route.includes(adjacent[r])) {
            route.push(adjacent[r])
            return auxGetRoute(adjacencyList, adjacent[r], vertex2, route)
        } 
    }

}

function textAreaToObject(txt) {
    let splitedTxt = txt.split('\n').filter(line => line.trim() != '')

    let adjacencyList = {}
    for (let i = 0; i < splitedTxt.length; i++) {
        let splitedLine = splitedTxt[i].split('->')
        let vertex = parseInt(splitedLine[0].trim())
        adjacencyList[vertex] = []
        for (let j = 1; j < splitedLine.length; j++) {
                if (splitedLine[j].trim() != '.') {
                    adjacencyList[vertex] = [...adjacencyList[vertex], parseInt(splitedLine[j].trim())]
                }
        }
    }
    return adjacencyList
}

function printMatrix(matrix) {
    let txtMatrix = matrix.reduce((acc, curr) => {
        let row = '|' + curr.reduce((acc1, curr1) => `${acc1} ` + `${curr1}`, '') + ' |<br/>'
        return `${acc} ` + `${row}`
    }, '')
    return txtMatrix

}
function onChange() {
    if (document.getElementById("use-examples").checked) {
        document.getElementById('example1').disabled = false
        document.getElementById('example2').disabled = false
        document.getElementById('example3').disabled = false
    } else {
        document.getElementById('example1').disabled = true
        document.getElementById('example2').disabled = true
        document.getElementById('example3').disabled = true
        document.getElementById('adjacency-list').value = ''
        document.getElementById('vertexes').value = ''
    }
}
function onFocusRadio(example) {
    let exampleAdjacecyLists = [ 
        '1 -> 2 -> 3 -> 4 -> .\n2 -> 4 -> .\n3 -> 1 -> 2 -> .\n4 -> .',
        '1 -> 2 -> 4 -> .\n2 -> 3 -> .\n3 -> .\n4 -> 3 -> 5 -> .\n5 -> .',
        '1 -> 2 -> 3 -> .\n2 -> 4 -> 5 -> .\n3 -> 6 -> .\n4 -> 7 -> .\n5 -> 7 -> .\n6 -> 5 -> 7 -> .\n7 -> .'
    ]

    let exampleVertexes = [
        '1, 2',
        '3, 1',
        '1, 7'
    ]

    document.getElementById('adjacency-list').value = exampleAdjacecyLists[example-1]
    document.getElementById('vertexes').value = exampleVertexes[example-1]

}
// let adjacencyList2 = {
//     1: [2,3,4],
//     2: [4],
//     3: [1,2],
//     4: [],
// }

// function exportGraph(adjacacyList) {

//     let amountOfVertexes = adjacacyList.length
//     let graph = {}
//     for (let v = 1; v <= amountOfVertexes; v++) {


//     }



// }


function readInputs() {

    if (document.getElementById('adjacency-list').value == '') {
        document.getElementById("error").innerHTML = "Erro! Você precisa inserir uma Lista de adjacencias no campo acima!."
    } else if (!document.getElementById('adjacency-list').value.includes('->')) {
        document.getElementById("error").innerHTML = "Erro! Lista de Ajdacências Invalida!."
    } else if (document.getElementById('vertexes').value.split(',').length > 2) {
        document.getElementById("error").innerHTML = "Erro! Você deve inserir no máximo dois vértices no campo acima!."

    } else {
        document.getElementById("error").innerHTML = ""
        let adjacencyList = document.getElementById('adjacency-list').value
        let vertexes = document.getElementById('vertexes').value.split(',')
        let vertex1 = parseInt(vertexes[0])
        let vertex2 = parseInt(vertexes[1])
        adjacencyList = textAreaToObject(adjacencyList)
        
        let matrix = getAdjacencyMatrix(adjacencyList)
        let [reachabilityMatrixPower, operationsPower] = powerFormula(matrix)
        let [reachabilityMatrixWarshall, operationsWarshall] = warshallAlgorithm(matrix)
        let vertexesAmount = amountOfVertexes(matrix)

        // Verifica se a Matriz de Adjacências foi marcada
        let adjacency_matrix_output = document.getElementById("adjacency-matrix-output")
        let adjacency_matrix_output_label = document.getElementById("adjacency-matrix-output-label")
        if (document.getElementById("adjacency-matrix").checked) {
            adjacency_matrix_output_label.innerHTML = "1 - Matriz de Adjacências:"
            adjacency_matrix_output.innerHTML = printMatrix(matrix)
        } else {
            adjacency_matrix_output.innerHTML = ""
            adjacency_matrix_output_label.innerHTML = ""
        }

        // Verifica se a Matriz de Alcançabilidade átraves da Fórmula de Potências foi marcada
        let alcancability_matrix_power_output = document.getElementById("alcancability-matrix-power-output")
        let alcancability_matrix_power_output_label = document.getElementById("alcancability-matrix-power-output-label")
        if (document.getElementById("alcancability-matrix-power").checked) {
            alcancability_matrix_power_output_label.innerHTML = "2 - Matriz de Alcançabilidade átraves da Fórmula de Potências:"
            alcancability_matrix_power_output.innerHTML = printMatrix(reachabilityMatrixPower)
        } else {
            alcancability_matrix_power_output.innerHTML = ""
            alcancability_matrix_power_output_label.innerHTML = ""
        }

        // Verifica se a Matriz de Alcançabilidade átraves do Algoritmo de Warshall foi marcada
        let alcancability_matrix_warshall_output = document.getElementById("alcancability-matrix-warshall-output")
        let alcancability_matrix_warshall_output_label = document.getElementById("alcancability-matrix-warshall-output-label")
        if (document.getElementById("alcancability-matrix-warshall").checked) {
            alcancability_matrix_warshall_output_label.innerHTML = "3 - Matriz de Alcançabilidade átraves do Algoritmo de Warshall:"
            alcancability_matrix_warshall_output.innerHTML = printMatrix(reachabilityMatrixWarshall)
        } else {
            alcancability_matrix_warshall_output.innerHTML = ""
            alcancability_matrix_warshall_output_label.innerHTML = ""
        }

        // Verifica se Vétices visitados a partir da Busca em Profundidade foi marcada
        let visited_vertexes_depth_search_output = document.getElementById("visited-vertexes-depth-search-output")
        let visited_vertexes_depth_search_output_label = document.getElementById("visited-vertexes-depth-search-output-label")
        if (document.getElementById("visited-vertexes-depth-search").checked) {
            visited_vertexes_depth_search_output_label.innerHTML = "4 - Vértices visitados a partir da Busca em Profundidade:"
            if (document.getElementById('vertexes').value == '') {
                visited_vertexes_depth_search_output.innerHTML = `Para visualizar esta resposta você precisa inserir pelo menos um vértice no campo acima.`
            }else {
                visited_vertexes_depth_search_output.innerHTML = `Os Vértices visitados foram: ${depthSearch(matrix, vertex1).reduce((acc, curr) => `${acc}, `+ `${curr}`)}.`
            }
        } else {
            visited_vertexes_depth_search_output.innerHTML = ""
            visited_vertexes_depth_search_output_label.innerHTML = ""
        }

        // Verifica se Vétices visitados a partir da Busca em Largura foi marcada
        let visited_vertexes_width_search_output = document.getElementById("visited-vertexes-width-search-output")
        let visited_vertexes_width_search_output_label = document.getElementById("visited-vertexes-width-search-output-label")
        if (document.getElementById("visited-vertexes-width-search").checked) {
            visited_vertexes_width_search_output_label.innerHTML = "5 - Vértices visitados a partir da Busca em Largura:"
            if (document.getElementById('vertexes').value == '') {
                visited_vertexes_width_search_output.innerHTML = `Para visualizar esta resposta você precisa inserir pelo menos um vértice no campo acima.`
            }else {
                visited_vertexes_width_search_output.innerHTML = `Os Vértices visitados foram: ${widthSearch(matrix, vertex1).reduce((acc, curr) => `${acc}, `+ `${curr}`)}.`
            }
        } else {
            visited_vertexes_width_search_output.innerHTML = ""
            visited_vertexes_width_search_output_label.innerHTML = ""
        }
        // Verifica se Quantidade de Vértices foi marcada
        let vertexes_amount_output = document.getElementById("vertexes-amount-output")
        let vertexes_amount_output_label = document.getElementById("vertexes-amount-output-label")
        if (document.getElementById("vertexes-amount").checked) {
            vertexes_amount_output_label.innerHTML = "6 - Quantidade de Vértices:"
            vertexes_amount_output.innerHTML = `Este Grafo possui ${vertexesAmount} Vértice${vertexesAmount == 1 ? '' : 's'}.`
        } else {
            vertexes_amount_output.innerHTML = ""
            vertexes_amount_output_label.innerHTML = ""
        }

        // Verifica se Quantidade de Arestas foi marcada
        let archs_amount_output = document.getElementById("archs-amount-output")
        let archs_amount_output_label = document.getElementById("archs-amount-output-label")
        if (document.getElementById("archs-amount").checked) {
            let archsAmount = amountOfArchs(matrix)
            archs_amount_output_label.innerHTML = "7 - Quantidade de Arestas:"
            archs_amount_output.innerHTML = `Este Grafo possui ${archsAmount} Aresta${archsAmount == 1 ? '' : 's'}.`
        } else {
            archs_amount_output.innerHTML = ""
            archs_amount_output_label.innerHTML = ""
        }

        // Verifica se Quantidade de Arestas que Saem e Chegam aos vértices foi marcada
        let how_many_come_in_out_output = document.getElementById("how-many-come-in-out-output")
        let how_many_come_in_out_output_label = document.getElementById("how-many-come-in-out-output-label")
        if (document.getElementById("how-many-come-in-out").checked) {
            how_many_come_in_out_output_label.innerHTML = "8 - Quantidade de Arestas que Saem e Chegam aos vértices:"
            if (document.getElementById('vertexes').value == '') {
                how_many_come_in_out_output.innerHTML = `Para visualizar esta resposta você precisa inserir pelo menos um vértice no campo acima.`
            }else {
                let comingOut = howManyComeOut(matrix, vertex1)
                let comingIn = howManyComeIn(matrix, vertex1)
                how_many_come_in_out_output.innerHTML = `Para  o vértice ${vertex1}: ${comingOut} aresta${comingOut == 1 ? '' : 's'} ${comingOut == 1 ? 'sai' : 'saem'} e ${comingIn} aresta${comingIn == 1 ? '' : 's'} ${comingIn == 1 ? 'chega' : 'chegam'}.`
            }
        } else {
            how_many_come_in_out_output.innerHTML = ""
            how_many_come_in_out_output_label.innerHTML = ""
        }

        // Verifica se Caminho entre os vértices informados (Se existir) foi marcada
        let verify_and_get_route_output = document.getElementById("verify-and-get-route-output")
        let verify_and_get_route_output_label = document.getElementById("verify-and-get-route-output-label")
        if (document.getElementById("verify-and-get-route").checked) {
            let route = getRoute(adjacencyList, reachabilityMatrixPower, vertex1, vertex2)
            verify_and_get_route_output_label.innerHTML = "9 - Caminho entre os vértices informados:"
            if (route == null) {
                verify_and_get_route_output.innerHTML = `Apenas um vértice foi informado!`
            } else if (!!route) {
                verify_and_get_route_output.innerHTML = `O Caminho do vértice ${vertex1} até o vértice ${vertex2} é: ${route.reduce((acc, curr) => `${acc} -> `+ `${curr}`)}.`
            }else {
                verify_and_get_route_output.innerHTML = `Não existe caminho desde o vértice ${vertex1} até o vértice ${vertex2}.`
            }
        } else {
            verify_and_get_route_output.innerHTML = ""
            verify_and_get_route_output_label.innerHTML = ""
        }

        // Verifica se Comparação da Complexidade foi marcada
        let complexity_output = document.getElementById("complexity-output")
        let complexity_output_label = document.getElementById("complexity-output-label")
        if (document.getElementById("complexity").checked) {
            let txtPower = `O total de operações através da Fórmula de Potências foi ${operationsPower}, enquanto na teoria seriam ${ 2 * ((vertexesAmount - 1) * vertexesAmount ** 3) + ((vertexesAmount - 1) * vertexesAmount ** 2)} operações.<br/>`
            let txtWarshall = `O total de operações através do Algoritmo de Warshall foi ${operationsWarshall}, enquanto na teoria seriam ${2 * vertexesAmount ** 3} operações.`

            complexity_output_label.innerHTML = "10 - Comparação da Complexidade (Operações E/OU):"
            complexity_output.innerHTML = txtPower + txtWarshall
        } else {
            complexity_output.innerHTML = ""
            complexity_output_label.innerHTML = ""
        }

    }
}

// readInputs()

// let adjacencyList = {
//     1: [2],
//     2: [3],
//     3: [1,4],
//     4: [],
//     5: [1,3]
// }
// let adjacencyList2 = {
//     1: [2,3,4],
//     2: [4],
//     3: [1,2],
//     4: [],
// }