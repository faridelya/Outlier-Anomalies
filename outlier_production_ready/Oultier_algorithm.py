from __future__ import division
from __future__ import print_function

from pyod.models.ecod  import ECOD
from data_loader import data_loader





def outlier_algorithm(data, Threshold=0.1 ):

  '''
  Parameters:

  Data:  data

  Threshold or contamination: float in (0., 0.5), optional (default=0.1)
  The amount of contamination of the data set, i.e. the proportion of outliers in the data set. Used when fitting to define the threshold on the decision function.

  Return : list of outlier
  

  '''
  data = data

  #BUILD aNOMALY MODEL
  #contamination = 0.1  # percentage of outliers
  # train COPOD detector
  clf_name = 'ECOD'
  clf = ECOD(contamination = Threshold )

  # you could try parallel version as well.
  # clf = COPOD(n_jobs=2)
  clf.fit(data)

  # get the prediction labels and outlier scores of the training data
  y_train_pred = clf.labels_  # binary labels (0: inliers, 1: outliers)
  y_train_scores = clf.decision_scores_  # raw outlier scores

  data["outlier_labels"] = y_train_pred
  outlier_list = data.index[data['outlier_labels'] == 1].tolist()
  

  return outlier_list
