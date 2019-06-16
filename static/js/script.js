var spterm = document.getElementById('spterm');

var searchArr = document.getElementsByClassName('search');

var search = document.getElementById('search');

search.onclick = function(){
    
    if(spterm.value == '' || spterm.value==null){
        for(var i = 0;i<searchArr.length;i++){
            searchArr[i].style.background = 'white';
            searchArr[i].style.color = 'black';

        }
    }
    else{
        for(var i = 0;i<searchArr.length;i++){
            searchArr[i].style.background = 'white';
            searchArr[i].style.color = 'black';
        }
        for(var i = 0;i<searchArr.length;i++){
            if(searchArr[i].children[1].innerHTML.toLowerCase().includes(spterm.value.toLowerCase())){
                searchArr[i].style.background = 'blue';
                searchArr[i].style.color = 'white';
            }
        }
    }
}



function fnExcelReport()
{
    var tab_text = '<table border="1px" style="font-size:20px" ">';
    var textRange;
    var j = 0;
    var tab = document.getElementById('headerTable'); // id of table
    var lines = tab.rows.length;

    // the first headline of the table
    if (lines > 0) {
        tab_text = tab_text + '<tr bgcolor="#DFDFDF">' + tab.rows[0].innerHTML + '</tr>';
    }

    // table data lines, loop starting from 1
    for (j = 1 ; j < lines; j++) {
        tab_text = tab_text + "<tr>" + tab.rows[j].innerHTML + "</tr>";
    }

    tab_text = tab_text + "</table>";
    tab_text = tab_text.replace(/<A[^>]*>|<\/A>/g, "");             //remove if u want links in your table
    tab_text = tab_text.replace(/<img[^>]*>/gi,"");                 // remove if u want images in your table
    tab_text = tab_text.replace(/<input[^>]*>|<\/input>/gi, "");    // reomves input params
    // console.log(tab_text); // aktivate so see the result (press F12 in browser)

    var ua = window.navigator.userAgent;
    var msie = ua.indexOf("MSIE ");

     // if Internet Explorer
    if (msie > 0 || !!navigator.userAgent.match(/Trident.*rv\:11\./)) {
        txtArea1.document.open("txt/html","replace");
        txtArea1.document.write(tab_text);
        txtArea1.document.close();
        txtArea1.focus();
        sa = txtArea1.document.execCommand("SaveAs", true, "DataTableExport.xls");
    }
    else // other browser not tested on IE 11
        sa = window.open('data:application/vnd.ms-excel,' + encodeURIComponent(tab_text));

    return (sa);
}

function exportToExcel(){
var htmls = "";
            var uri = 'data:application/vnd.ms-excel;base64,';
            var template = '<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:x="urn:schemas-microsoft-com:office:excel" xmlns="http://www.w3.org/TR/REC-html40"><head><!--[if gte mso 9]><xml><x:ExcelWorkbook><x:ExcelWorksheets><x:ExcelWorksheet><x:Name>{worksheet}</x:Name><x:WorksheetOptions><x:DisplayGridlines/></x:WorksheetOptions></x:ExcelWorksheet></x:ExcelWorksheets></x:ExcelWorkbook></xml><![endif]--></head><body><table>{table}</table></body></html>';
            var base64 = function(s) {
                return window.btoa(unescape(encodeURIComponent(s)))
            };

            var format = function(s, c) {
                return s.replace(/{(\w+)}/g, function(m, p) {
                    return c[p];
                })
            };

            htmls = "YOUR HTML AS TABLE"

            var ctx = {
                worksheet : 'Worksheet',
                table : htmls
            }


            var link = document.createElement("a");
            link.download = "export.xls";
            link.href = uri + base64(format(template, ctx));
            link.click();
}

