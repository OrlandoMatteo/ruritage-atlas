function addSIA() {

	sia_col=document.getElementById('sia_col');
	

	if (sia_col.style.display=='none') {
		sia_col.style.display='block'
	}
	else{
		sia_col.style.display='none'	
	}
	//sia_btn=document.getElementById('sia_btn')
	$("#sia_btn").toggleClass("btn btn-primary btn btn-secondary")


}
function addCC() {
	cc_col=document.getElementById('cc_col');

	if (cc_col.style.display=='none') {
		cc_col.style.display='block'
	}
	else{
		cc_col.style.display='none';
	}
	$("#cc_btn").toggleClass("btn btn-primary btn btn-secondary")
}

function updateResult() {
	var sias=[];
	var ccs=[];

	checkboxesSIA=document.getElementById('sia_col');
    for (i=0;i<checkboxesSIA.children.length;i++){
        if (checkboxesSIA.children[i].type=="checkbox")
        {
            if (checkboxesSIA.children[i].checked)
            {
                sias.push(checkboxesSIA.children[i].value);
            }
        }
    }
    checkboxesCC=document.getElementById('cc_col');
    for (i=0;i<checkboxesCC.children.length;i++){
        if (checkboxesCC.children[i].type=="checkbox")
        {
            if (checkboxesCC.children[i].checked)
            {
                ccs.push(checkboxesCC.children[i].value);
            }
        }
    }

    var queryResult=$.ajax({
        method: 'GET',      
        url: "/queryBP",
        data: {SIAs:JSON.stringify(sias), CCs:JSON.stringify(ccs)},
        dataType: 'json',

        success: function(response) {
            x=response;
            populateTable(x);
            
    }});
    console.log('map updated!')
}

function populateTable(BPJson) {
	$('#result').empty();
	row='<tr>'
	for (var i = 0; i < BPJson.BestPractices.length; i++) {
		console.log(BPJson.BestPractices[i])
		row+='<th>'+BPJson.BestPractices[i].BPName+'</th>'+'<th>'+BPJson.BestPractices[i].RM+'</th>'+'<th>'+BPJson.BestPractices[i].SIA+'</th>'+'<th>'+BPJson.BestPractices[i].CCs.toString()+'</th></tr>'
		$('#result').append(row);
		row='<tr>';
	}
}