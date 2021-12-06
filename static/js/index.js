// let activeBtn = document.getElementById("eventsBtn");
// let codeLib = document.getElementById("eventsCodeLib");
let codePanel = document.getElementsByClassName("panel");

let btns = document.getElementsByClassName("codeGroupBtn");

let canvas = document.getElementById("canvas");

let dragElem = document.getElementsByClassName("dragElement");
let dragStart = document.getElementsByClassName("start")[0];

let toggle = 0;
let last = -1;

let colors = [
    "#6388f1","#68cdff","#fbbda2","#77e354","#f5b768","#ffd263","#7d68f1","#f08f63","#51e3c3"
];

let codeJson = [];

let outputArea = document.getElementById("outputText");
outputArea.rows = 38;

let clearBtn = document.getElementById("clear");

let runBtn = document.getElementById("run");

let codes = [];

let canvaNodes = [];

for (let j=0; j<btns.length; j++){
    (function (index) {
        let btn = btns[index];
        btn.addEventListener('click', function (e) {
            toggleFocus(e,index);
        })
    }(j));
}

function toggleFocus(event,i){
    if (last != -1){
        if (toggle == 1){               // 当前展开
            if (last == i){             // 点击了展开的这个
                btns[i].blur();
                btns[i].style.background = "#0000";
                btns[i].lastElementChild.style.color = "#7e683b";
                codePanel[i].style.display = "none";
                toggle = 0;
            }
            else {
                btns[last].blur();
                btns[last].style.background = "#0000";
                btns[last].lastElementChild.style.color = "#7e683b";
                codePanel[last].style.display = "none";
                btns[i].focus();
                btns[i].style.background = colors[i];
                btns[i].lastElementChild.style.color = "#fff";
                codePanel[i].style.display = "block";
            }
        }
        else {                          // 当前未展开
            btns[i].focus();
            btns[i].style.background = colors[i];
            btns[i].lastElementChild.style.color = "#fff";
            codePanel[i].style.display = "block";
            toggle = 1;
        }
    }
    else {
        console.log('run');
        console.log(i);
        btns[i].focus();
        btns[i].style.background = colors[i];
        btns[i].lastElementChild.style.color = "#fff";
        codePanel[i].style.display = "block";
        toggle = 1;
    }
    last = i;
}

function close(){
    btns[last].blur();
    btns[last].style.background = "#0000";
    btns[last].lastElementChild.style.color = "#7e683b";
    codePanel[last].style.display = "none";
    toggle = 0;
}


canvas.addEventListener("drop", function (e){
    e.preventDefault();
    let data = e.dataTransfer.getData("Text");
    let index = e.dataTransfer.getData("num");
    console.log(data,index);
    let node = document.getElementsByClassName(data)[0];
    console.log(node);

    let clone = node.cloneNode(true);
    clone.style.background = colors[last];
    e.target.appendChild(clone);
    canvaNodes.push(clone);
    for (let sonElement of clone.children) {
        if (sonElement.tagName === 'INPUT') {
            console.log(sonElement.value)
        }
    }

    close();

});



canvas.addEventListener("dragover", function (e){
    e.preventDefault();
});




for(let i=0; i<dragElem.length; i++){
    dragElem[i].addEventListener("dragstart", function (e) {
        e.dataTransfer.setData("text", e.target.className);
        e.dataTransfer.setData("num",last);
    });

}

clearBtn.addEventListener("click",function (event){
    outputArea.textContent = "";
});



runBtn.addEventListener("click", function (e){
    setData(canvaNodes);
    // print(codes);
    console.log("============");
    console.log(codes);
});


$(document).ready(function (){
    $('form').on('submit', function (event){
        console.log(JSON.stringify(codes));
        $.ajax({
            data: JSON.stringify(codes),
            type: 'POST',
            url: '/process'
        })
            .done(function (data) {
                // console.log('cock robin');
                $('#outputText').text(data.output).show();
            });
        event.preventDefault();
    });
});

// json
/*
{
"类型": {
        "缩进",
        "参数1"，
        "参数2"，
        "参数m",
}
*/


function setData(nodes) {
    codes = []
    for (let node of nodes) {
        let code = [];
        // code.append(1);
        console.log(node);
        console.log(node.id);
        code.push(node.id);

        let tab = 0;
        let tmpNode = node;
        let parent = [];
        let append = 1;
        while (tmpNode.parentNode != canvas){
            tmpNode = tmpNode.parentNode;
            if (append){
                for (let i=0; i<nodes.length; i++) {
                    if (nodes[i] === tmpNode){
                        parent.push(i);
                        break;
                        }
                }
                append = 0;
            }
            // parent.push(tmpNode);
            tab += 1
        }
        parent.push(tab);
        parent.reverse();

        code.push(parent);

        for (let elem of node.children){
            if (elem.tagName === 'INPUT'){
                code.push(elem.value)
            }
        }
        // code.push(info);
        codes.push(code);
    }
}




















