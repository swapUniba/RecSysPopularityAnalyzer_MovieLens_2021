# RecSysPopularityAnalyzer_MovieLens_2021
Analisi della fairness e popularity bias nei RecSys in MovieLens, realizzato nel lavoro di tesi di Valletta Antonio.


## Framework per l'analisi della fairness e popularity bias in MovieLens
<p> Il seguente framework, permette l'esecuzione di diversi algoritmi di tipo: Collaborative Filtering, Content-based Word Embedding e Graph-based.
    All'interno, vi sono anche degli script per il calcolo di metriche e la generazione di grafici utili all'analisi del comportamento delle varie tecniche nel dataset,             partendo, dunque, dalle raccomandazioni generate da ciascun algoritmo.
  
 Nel dettaglio, tale framework presenta i seguenti moduli:
  - **Collaborative Filtering**: per l'esecuzione dei diversi algoritmi collaborativi offerti dalla libreria Lenskit;
  - **Content-based Word Embedding**: per l'esecuzione dei diversi algoritmi Content-based con tecniche di Word-embedding offerte dalla libreria Gensim;
  - **Pagerank e Personalized Pagerank**:  per l'esecuzione di algoritmi graph-based, ovvero Pagerank e Pagerank personalizzato (creazione del grafo e calcolo del pagerank,         grazie alla libreria NetworkX);
  - **Analysis**: calcolo di metriche, generazione di grafici e suddivisione degli utenti nelle tre sottocategorie: Cold-Start, Hot-Start e Regular;
  - **Utils**: per il mapping dei contenuti testuali, splitting degli utenti e altre operazioni di supporto;
  - **Convertion**: utile alla conversione di file parquet in file CSV.
  
  Per l'esecuzione, ci si è serviti del seguente dataset:
  - **MovieLens**:  https://1drv.ms/u/s!AjfPOmmKNJRdnBibCprJTSripSzw?e=avGcLD (contenente i dati con cui le precedenti raccomandazioni sono state generate: MovieLens1M, descrizioni, generi, tags, lista item popolari, suddivisione degli utenti)
  
  ## Installazione
  - *STEP 1*: Assicurarsi di disporre di una versione Python 3.6 o successiva;
  - *STEP 2*: Aprire il terminale e digitare `pip install numpy scipy pandas sklearn lenskit gensim matplotlib networkx implicit levenshtein`
  
  ## Configurare ed eseguire gli algoritmi
  ### Collaborative Filtering
  Per calcolare le raccomandazioni generate dagli algoritmi collaborativi è necessario lanciare lo script **run.py** all'interno di questo modulo. A differenza di tutte le     altre tecniche di raccomandazione, questo scrit esegue tutti gli algoritmi e serializza i diversi risultati in un file *.parquet*. Per tal ragione, potrebbe essere utile     convertire tali file in *.csv* per il successivo calcolo di metriche/grafici e suddivisione nelle 3 sottocategorie di utenti (mediante il modulo *convertion*).
  
  ### Content-based Word Embedding
  Questo modulo presenta all'interno uno script chiamato **run.py**, per l'esecuzione dei rispettivi algoritmi. All'interno, vi è una sezione di configurazione dei parametri   con la quale si vuole che l'algoritmo venga lanciato (Esempio: numero di raccomandazioni per utente, algoritmo da utilizzare, settaggio di descrizioni-tags-generi ecc...).
  
  ### Pagerank e Personalized Pagerank
  Questi due moduli presentano all'interno uno script chiamato run.py per l'esecuzione dei rispettivi algoritmi. Anche in questo caso, all'interno di tali script vi e' una     sezione per la configurazione dei parametri con cui si vuole che gli algoritmi vengano lanciati.
  
  ### Calcolo delle metriche e generazione grafici 
  All'interno del modulo *Analysis*, vi è uno script **run.py** per il calcolo di metriche e la generazione di grafici, partendo dalle raccomandazioni generate da uno           specifico algoritmo Content-based Word Embedding o Graph-based. All'interno, è possibile trovare una sezione di configurazione dei parametri, all'interno della quale va       indicato: 
  - nome dell'algoritmo (per il quale calcolare metriche e generare grafici);
  - percorso da cui reperire le raccomandazioni;
  - path del dataset utilizzato.
  
 Per gli algoritmi collaborativi, invece, è necessario lanciare lo script **run_cf.py**, considerata la differente modalità con la quale Lenskit serializza i risultati.
  
  ### Suddivisione degli utenti
  Il modulo *Analysis* presenta lo script **run_us.py** per la suddivisione degli utenti nelle tre sottocategorie: Cold-Start, Hot-Start, Regular. Al suo interno, vi è una     sezione di configurazione dei parametri, nella quale va indicato:
  - nome del file di raccomandazione generato da uno specifico algoritmo (CF, CB-Word Embedding o Graph-based);
  - percorso dal quale recuperare tali raccomandazioni;
  - path nella quale salvare i risultati;
  - categoria (Cold, Hot, Regular).
  
  
  
    

